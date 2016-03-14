PERCENTAGES = {"32": .0005, "16": .0175, "8": .0425, "4": .12, "2":.15, "1":.22}

class Pot(object):
	def __init__(self, value=0, numteams=0, estimate=2800):
		self.value = value
		self.numteams = numteams

	def num_teams(self):
		return self.numteams

	def get_value(self):
		return self.value

	def get_estimate(selt):
		return self.estimate

	def add_team(self, value):
		self.value += value
		self.numteams += 1

	def update_estimate(self, estimate):
		self.estimate = estimate


class teamOdds(object):
	def __init__(self, name, pct32, pct16, pct8, pct4, pct2, pct1):
		self.name = name
		self.pct32 = pct32
		self.pct16 = pct16
		self.pct8 = pct8
		self.pct4 = pct4 
		self.pct2 = pct2
		self.pct1 = pct1

	def __str__(self):
		return "%s has a %s pct chance to reach rd32, %s to reaching sweet 16, %s to reach elite 8, %s to reach final four, %s to be runner up, and %s to win the ship " %(self.name, self.pct32, self.pct16, self.pct8, self.pct4, self.pct2, self.pct1)
	#need to come up with the algorithm to calculate expected value based on the different odds. 
	

	##given the odds of reaching each round and the current size of the pot (or an estimate), determine a teams payout
	##uses expected value to determine payout based on the pot.
	#def predict_payout(self, pot):



def calc_current_payouts(pot):
	print "Payouts based on current pot for being eliminated in the following rounds:"
	print "Round of 32: %d" % (pot.get_value() * PERCENTAGES['32'])
	print "Sweet Sixteen %d" % (pot.get_value() * PERCENTAGES['16'])
	print "Elite Eight: %d" % (pot.get_value() * PERCENTAGES['8'])
	print "Final four: %d" % (pot.get_value() * PERCENTAGES['4'])
	print "Runner up: %d" % (pot.get_value() * PERCENTAGES['2'])
	print "National Champion: %d" % (pot.get_value() * PERCENTAGES['1'])


	print "Payouts based on estimated pot for being eliminated in the following rounds:"
	print "Round of 32: %d" % (pot.get_estimate() * PERCENTAGES['32'])
	print "Sweet Sixteen %d" % (pot.get_estimate() * PERCENTAGES['16'])
	print "Elite Eight: %d" % (pot.get_estimate() * PERCENTAGES['8'])
	print "Final four: %d" % (pot.get_estimate() * PERCENTAGES['4'])
	print "Runner up: %d" % (pot.get_estimate() * PERCENTAGES['2'])
	print "National Champion: %d" % (pot.get_estimate() * PERCENTAGES['1'])

	return



odds538 = {}
oddsKenPom = {}



#function for manual input
def build_team_odds(dictionary):
	#ask for team name, followed by all percentages.
	#create a teamOdds object and add it to a dictionary
	#return the dictionary

	name = raw_input("Please enter the team name: ")

	if (name == "stop"):
		return 0

	r32 = raw_input("Please enter the chance of making it to the round of 32: ")
	r16 = raw_input("Please enter the chance of making it to the round of 16: ")
	r8 = raw_input("Please enter the chance of making it to the elite 8: ")
	r4 = raw_input("Please enter the chance of making it to the final four: ")
	r2 = raw_input("Please enter the chance of being runner up: ")
	r1 = raw_input("Please enter the chance of winning the tournament: ")


	dictionary[name] = teamOdds(name, r32, r16, r8, r4, r2, r1)

	return 1


#takes a teamname and a dollar value of a pot and determines the predicted payout
def getestvalue(teamname, potvalue):
	print "Using 538s odds, the predicted payout of %s is %d" % (teamname, odds538[teamname].predict_payout(pot))
	print "Using KenPom odds, the predicted payout of %s is %d" % (teamname, oddsKenPom[teamname].predict_payout(pot))
	return

##need to write a fucntion that combines the 13-16s and names them by region
#def combine_13-16s(dictionary)


#write a function to somehow estimate what the entire pot will be based on the current pot


#write a function that calculates ROI



#function designed to read data copy-pasted from the KenPom website
def read_KenPom():
	with open('kenpom.txt') as f:
		for line in f:
			linetemp = line.split()
			if linetemp[2][0].isalpha():
				linetemp[1] = linetemp[1] + " " + linetemp[2]
				linetemp.pop(2)
			linetemp[1] = linetemp[1].lower()
			#print linetemp
			oddsKenPom[linetemp[1]] = teamOdds(linetemp[1], linetemp[2], linetemp[3], linetemp[4], linetemp[5], linetemp[6], linetemp[6])

read_KenPom()









