import socket #helps connect to twitch
import threading #allows us to stay connected to twitch while we issue commands to PC
import time
from ahk import AHK #sends commands to computer

#Download Autohotkey at https://www.autohotkey.com/ and provide the address to
#AutoHotkey.exe below!
ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')

SERVER = "irc.twitch.tv"
PORT = 6667

#Your OAUTH Code Here https://twitchapps.com/tmi/
PASS = "oauth:1843s0n1e7c6c9k2tfipfvz9sgyya2"

#What you'd like to name your bot
BOT = "TwitchBot"

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

	def chatCommands(message):
		if '!test' == message:
			sendMessage(irc, 'True')
			message = ""

			#!fight
			#!shot
			#!focus
			#!bomb
			#!dodge
			#!mystats
			#!score
			#!taunt

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

	def getUser(line):
		#global user
		colons = line.count(":")
		colonless = colons-1
		separate = line.split(":", colons)
		user = separate[colonless].split("!", 1)[0]
		return user

	#def initUser(line):
	#	userInfo = [user, character, party, lives, bombs, Stype, Ftype, Btype, score]
	#	return userInfo
		#I need some file to store all the user info
		#In this file, check if the user exists
		#If exists, retrieve data
		#If doesn't exist, initialize data:
		#init = [user, character(e.g. Reimu), party(possible characters), #lives, #bombs, Stype, Ftype, Btype, score]

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