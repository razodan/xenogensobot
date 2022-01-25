#CHARACTER CLASS FILE
#FOR INSTANCES OF CHARACTER OBJECTS

class Character(object):
	def __init__(self,name):
		self.name = name

		self.shotInt = 0
		self.focusInt = 0
		self.bombInt = 0

		self.shotType = "none" #make possible range from 0 - 3
		self.focusType = "none" #possible range from 0 - 4
		self.bombType = "none" #possible range from 0 - 4
		self.taunts = []
		self.sign = ""

		#how to make this work?

	def updateTaunt(self, taunt):
		self.taunts.append(taunt)

	def updateSign(self, sign):
		self.sign = sign

	def setShot(self, shotInt):
		self.shotInt = shotInt
		if self.shotInt == 1:
			self.shotType = "Straight"
		elif self.shotInt == 2:
			self.shotType = "Homing"
		elif self.shotInt == 3:
			self.shotType = "Spread"

	def setFocus(self, focusInt):
		self.focusInt = focusInt
		if self.focusInt == 1:
			self.focusType = "Straight"
		elif self.focusInt == 2:
			self.focusType = "Homing"
		elif self.focusInt == 3:
			self.focusType = "Spread"
		elif self.focusInt == 4:
			self.focusType = "Special"

	def setBomb(self, bombInt):
		self.bombInt = bombInt
		if self.bombInt == 1:
			self.bombType = "Straight"
		elif self.bombInt == 2:
			self.bombType = "Homing"
		elif self.bombInt == 3:
			self.bombType = "Barrier"
		elif self.bombInt == 4:
			self.bombType = "Negation"

	#how to store private data and taunt info in python?

Reimu = Character('Reimu Hakurei') #s2 homing, f1 straight, b2 homing
Marisa = Character('Marisa Kirisame') #s1 straight, f1 straight, b2 straight
Sakuya = Character('Sakuya Izayoi') #s1 spread, f4 special, b4 negation

#############################################
###				REIMU HAKUREI			  ###
#############################################
Reimu.setShot(2)
Reimu.setFocus(1)
Reimu.setBomb(2)
Reimu.updateTaunt("Me? Lessee... I'm Reimu Hakurei. Shrine maiden.")
Reimu.updateTaunt("Ah, idiot sighted. Are planning to do something bad?")
Reimu.updateTaunt("Hey, you look like you want me to beat you. What do they call that? Sadism?")
Reimu.updateSign("I'm the Hakurei Shrine maiden who silences crying children! Spirit Sign, FANTASY SEAL!!")
print(Reimu.name + ", shot type: " + Reimu.shotType + ", focus type: " + Reimu.focusType + ", bomb type: " + Reimu.bombType)

#############################################
###				MARISA KIRISAME			  ###
#############################################
Marisa.setShot(1)
Marisa.setFocus(1)
Marisa.setBomb(1)
Marisa.updateTaunt("I'm Marisa Kirisame. Jus' an ordinary magician. A /very/ ordinary magician.")
Marisa.updateTaunt("Goodbye. I'll pray for your happiness in the next world. ...Whoops, killed you off too early!<3")
Marisa.updateTaunt("You got any books? I'll hafta borrow some later. Yeah, I'm gonna take 'em.")
Marisa.updateSign("It ain't magic if it ain't flashy! Love Sign, MASTER SPARK!!")
print(Marisa.name + ", shot type: " + Marisa.shotType + ", focus type: " + Marisa.focusType + ", bomb type: " + Marisa.bombType)

#############################################
###				SAKUYA IZAYOI	       	  ###
#############################################
Sakuya.setShot(3)
Sakuya.setFocus(4)
Sakuya.setBomb(4)
Sakuya.updateTaunt("My, my... what a mess to clean up. This won't take long.")
Sakuya.updateTaunt("Ah, I only packed three sets of clothes. And one set of knives.")
Sakuya.updateTaunt("Get back to work! ...Ah, forgive me. I thought you were a fairy maid.")
Sakuya.updateSign("Oh? You're approaching me? In that case... Illusion World Sign, THE WORLD!!")
print(Sakuya.name + ", " + "shot type: " + Sakuya.shotType + ", focus type: " + Sakuya.focusType + ", bomb type: " + Sakuya.bombType)

#When using a bomb, character calls out the spell card name
#Sakuya: The world. Stop time.
#Marisa: Love-coloured sign, Master Spark!
#Reimu: Fantasy sign, Fantasy Seal!

	#INFORMATION
	#SHOT TYPE
		#1 = Straight - low accuracy, low dmg
		#2 = Homing - high accuracy, low dmg
		#3 = Spread - mid accuracy, low dmg
	#FOCUS TYPE
		#1 = Straight
		#2 = Homing
		#3 = Spread
		#4 = Special
	#BOMB TYPE
		#1 = Straight - chance to negate shot, high dmg
		#2 = Homing - chance to negate shot, high dmg
		#3 = Barrier - negate shot + chance to negate next shot, no dmg
		#4 = Negation - negate shot, mid dmg