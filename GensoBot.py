import socket #helps connect to twitch
import threading #allows us to stay connected to twitch while we issue commands to PC
import csv

SERVER = "irc.twitch.tv"
PORT = 6667

#Your OAUTH Code Here https://twitchapps.com/tmi/
PASS = "oauth:btemk0ax3x0q8frl80assxrq5xxe1e"

#What you'd like to name your bot
BOT = "GensoBot"

#The channel you want to monitor
CHANNEL = "xenoprism"

#Your account
OWNER = "xenoprism"

message = ""
user = ""

irc = socket.socket()

irc.connect((SERVER, PORT))
irc.send((	"PASS " + PASS + "\n" +
			"NICK " + BOT + "\n" +
			"JOIN #" + CHANNEL + "\n").encode())

def twitch():

	global user
	global message

	header = ['user', 'character', 'members', 'score', 'lives', 'bombs']
	rows = []
	filename = "userData.csv"

	#make a list of Player objects. Access list. If Player object not in list, then initialize new Player object.
	#else, update Player stuff after each command

	with open(filename, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(header)

	def chatCommands(message):
		if '!test' == message:
			sendMessage(irc, 'True')
			message = ""

		if '!battle' == message:
			sendMessage(irc, 'fight command')
			message = ""

		if '!accept' == message:
			sendMessage(irc, 'accept command')
			message = ""

		if '!shot' == message:
			sendMessage(irc, 'player1 fires a shotType at player2!')
			message = ""

		if '!focus' == message:
			sendMessage(irc, 'player1 fires a focusType at player2!')
			message = ""

		if '!bomb' == message:
			sendMessage(irc, 'player1 unleashes a spell card at player2!') #then, activate the Character.printSign() function
			message = ""

		if '!dodge' == message:
			sendMessage(irc, 'player1 attempts to dodge!') #then do some calculations. Three outcomes: dodge failed, dodge successful, or GRAZE
			message = ""

		if '!mystats' == message:
			sendMessage(irc, 'stats') #display current character, score, lives, and bombs
			message = ""

		if '!party' == message:
			#first, check for party number. 0 = Reimu & Marisa /// 1 = 0 + Youmu & Sakuya /// 2 = 1 + Reisen & Sanae /// 3 = 2 + Cirno & Aya /// 4 = 3 + Koishi & Hata no Kokoro
			sendMessage(irc, 'available party members...') #display available party members
			message = ""

		if '!score' == message:
			sendMessage(irc, 'display score -- ')
			message = ""

		if '!taunt' == message:
			sendMessage(irc, 'randomly select a taunt from current Character object')
			message = ""

		if '!actions' == message:
			sendMessage(irc, '!battle = initiate battle scene. || !accept = accept fight. || !shot = normal shot attack. || !focus = focus shot attack. || !bomb = spell card attack. || !dodge = attempt to dodge. || !taunt = taunt your enemy. || !mystats = check stats. || !party = check available Characters. || !score = check current score. || !actions = view this list.')

			#!battle
			#!accept
				#!shot
				#!focus
				#!bomb
				#!dodge
				#!taunt
			#!mystats
			#!party
			#!score
			#!actions

			#username, character, partymembers, lives, bombs, Stype, Ftype, Btype, score
				
				#1: Reimu Hakurei
				#2: Marisa Kirisame

				
				#3: Youmu Konpaku
				#4: Sakuya Izayoi
				
				
				#5: Reisen Udongein Inaba
				#6: Sanae 
				
				
				#7: Cirno
				#8: Clownpiece

			#DO HERE?#

	def joinchat():
		Loading = True
		while Loading:
			readbuffer_join = irc.recv(1024)
			readbuffer_join = readbuffer_join.decode()
			print(readbuffer_join)
			for line in readbuffer_join.split("\n")[0:-1]:
				print(line)
				Loading = loadingComplete(line)

	def loadingComplete(line):
		if("End of /NAMES list" in line):
			print("GensoBot has joined " + CHANNEL + "'s Channel!")
			sendMessage(irc, "Successfully connected.")
			return False
		else:
			return True

	def sendMessage(irc, message):
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
		irc.send((messageTemp + "\n").encode())

	def newUser(name):
		newline = [name, 'Reimu Hakurei', '0', '0', '3', '1']
		rows.append(newline)
		print(rows)
		#csvwriter.writerow(newline)

	def getUser(line):
		#global user
		colons = line.count(":")
		colonless = colons-1
		separate = line.split(":", colons)
		user = separate[colonless].split("!", 1)[0]
		return user
		#I need some file to store all the user info
		#In this file, check if the user exists
		#If exists, retrieve data
		#If doesn't exist, initialize data:
		
	def getMessage(line):
		#global message
		try:
			colons = line.count(":")
			message = (line.split(":", colons))[colons]
		except:
			message = ""
		return message

	def console(line):
		if "PRIVMSG" in line:
			return False
		else:
			return True

			########################################################

	joinchat()
	irc.send("CAP REQ :twitch.tv/tags\r\n".encode())
	while True:
		try:
			readbuffer = irc.recv(1024).decode()
		except:
			readbuffer = ""
		for line in readbuffer.split("\r\n"):
			if line == "":
				continue
			if "PING :tmi.twitch.tv" in line:
				print(line)
				msgg = "PONG :tmi.twitch.tv\r\n".encode()
				irc.send(msgg)
				print(msgg)
				continue
			else:
				try:
					user = getUser(line)
					print(user)
					# if user not in rows:
					# 	try:
					# 		newUser(user)
					# 		print("newUser succeeded")
					# 	except Exception:
					# 		print("newUser failed")
					# 		pass	
					message = getMessage(line)
					print(user + " : " + message)
					chatCommands(message)
				except Exception:
					pass

def main():
	if __name__ =='__main__':
		t1 = threading.Thread(target = twitch)
		t1.start()
main()