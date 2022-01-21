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

		#how to make this work?

	def updateTaunt(self, taunt):
		self.taunts.append(taunt)

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

Reimu.setShot(2)
Reimu.setFocus(1)
Reimu.setBomb(2)
Reimu.updateTaunt("I'm the Hakurei shrine maiden who silences crying children!")
Reimu.updateTaunt("Taunt #2")
Reimu.updateTaunt("Taunt #3")
print(Reimu.taunts[0])
print(Reimu.taunts[1])
print(Reimu.taunts[2])
print(Reimu.name + ", shot type: " + Reimu.shotType + ", focus type: " + Reimu.focusType + ", bomb type: " + Reimu.bombType)

Marisa.setShot(1)
Marisa.setFocus(1)
Marisa.setBomb(1)
Marisa.updateTaunt("I've only eaten bread 13 times in my life. I prefer Japanese food.")
Marisa.updateTaunt("KLEPTO TAUNT")
Marisa.updateTaunt("Mushrooms")
print(Marisa.name + ", shot type: " + Marisa.shotType + ", focus type: " + Marisa.focusType + ", bomb type: " + Marisa.bombType)

Sakuya.setShot(3)
Sakuya.setFocus(4)
Sakuya.setBomb(4)
Sakuya.updateTaunt("My, my... what a mess to clean up. This won't take long.")
Sakuya.updateTaunt("My mistress is not to be disturbed. Begone.")
Sakuya.updateTaunt("Get back to work! ...Ah, forgive me. I thought you were a fairy maid.")
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
