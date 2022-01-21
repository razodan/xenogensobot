import socket #helps connect to twitch
import threading #allows us to stay connected to twitch while we issue commands to PC
import csv

SERVER = "irc.twitch.tv"
PORT = 6667

#Your OAUTH Code Here https://twitchapps.com/tmi/
PASS = "oauth:gajmx6oackfik1mcq5i645zuhxvk2j"

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

	fields = ['user', 'character', 'members', 'score', 'lives', 'bombs']
	filename = "userData.csv"
	rows = [ [] ]

	with open(filename, 'w') as csvfile:
		csvwriter = csv.writer(filename)
		csvwriter.writerow(fields)
		csvfile.close()

	global user
	global message

	def chatCommands(message):
		if '!test' == message:
			sendMessage(irc, 'True')
			message = ""

			#!fight
			#!accept
				#!shot
				#!focus
				#!bomb
				#!dodge
			#!mystats
			#!score
			#!taunt
			#!actions

			#username, character, partymembers, lives, bombs, Stype, Ftype, Btype, score
				
				#1: Reimu Hakurei
				#2: Marisa Kirisame

				
				#3: Youmu Konpaku
				#4: Sakuya Izayoi
				
				
				#5: Reisen Udongein Inaba
				#6: Sanae 
				
				
				#7: Cirno
				#8: Aya Shameimaru

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
			print("TwitchBot has joined " + CHANNEL + "'s Channel!")
			sendMessage(irc, "Successfully connected.")
			return False
		else:
			return True

	def sendMessage(irc, message):
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
		irc.send((messageTemp + "\n").encode())

	def newUser(name):
		newline = [name, 'Reimu Hakurei', '0', '0', '3', '3']
		rows.append(newline)
		csvwriter.writerow(newline)

	def getUser(line):
		#global user
		colons = line.count(":")
		colonless = colons-1
		separate = line.split(":", colons)
		user = separate[colonless].split("!", 1)[0]

		with open(filename, 'w') as csvfile:
			csvfilewriter = csv.writer(csvfile)
			if user not in rows:
				newUser(user)
			csvfile.close()

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
					message = getMessage(line)
					print(user + " : " + message)
					print(message)

					chatCommands(message)

					#DO HERE?#


				except Exception:
					pass

def main():
	if __name__ =='__main__':
		t1 = threading.Thread(target = twitch)
		t1.start()
main()