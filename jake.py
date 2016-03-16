PERCENTAGES = {"32": .005, "16": .0175, "8": .0425, "4": .12, "2":.16, "1":.16}


#NEED TO ADD THE PLAY IN 16 SEED WINNERS
LOWERSOUTH = ['austin peay', 'unc asheville', 'buffalo', 'hawaii']
LOWERWEST = ['csu bakersfield', 'green bay', 'unc wilmington', 'holy cross', 'southern'] 
LOWERMIDWEST = ['hampton', 'middle tennessee', 'fresno st.', 'iona']
LOWEREAST = ['weber st.', 's. f. austin', 'stony brook', 'fcgu', 'f. dickinson']

PREVIOUS = 1826.0
PREVIOUS_BIDS_AFTER4S = [0.0, 40.0, 94.0, 174.0, 258.0, 321.0, 403.0, 529.0, 642.0, 783.0, 1000.0, 1295.0, 1700.0, 2553.0]
class Pot(object):
	def __init__(self, value=0, numteams=0, previous=PREVIOUS):
		self.value = value
		self.numteams = numteams
		self.estimate = previous

	def num_teams(self):
		return self.numteams

	def get_value(self):
		return self.value

	def get_estimate(self):
		return self.estimate

	def add_team(self, value):
		self.value += value
		self.numteams += 1
		# if (self.numteams % 4) == 0:
		# 	self.update_estimate(self.numteams/4)

	#need to write this fn to calculate based on previous
	def update_estimate(self, spot):
		curval = self.value
		preval = PREVIOUS_BIDS_AFTER4S[spot]
		ratio = curval/preval
		self.estimate = PREVIOUS * ratio

		


class teamOdds(object):
	def __init__(self, name, pct32 = 0, pct16 = 0, pct8 = 0, pct4 = 0, pct2 = 0, pct1 = 0):
		self.name = name
		self.pct0win = 100.0 - float(pct32)
		self.pct1win = float(pct32) - float(pct16)
		self.pct2win = float(pct16) - float(pct8)
		self.pct3win = float(pct8) - float(pct4)
		self.pct4win = float(pct4) - float(pct2)
		self.pct5win = float(pct2) - float(pct1)
		self.pct6win = float(pct1)
		

		self.baiScore = self.pct1win * PERCENTAGES['32'] + self.pct2win * PERCENTAGES['16'] + self.pct3win * PERCENTAGES['8'] + self.pct4win * PERCENTAGES['4'] + self.pct5win * PERCENTAGES['2'] + self.pct6win * PERCENTAGES['1'] 
	

	def __str__(self):
		return "%s has a Bai Score of %s. A %s pct chance to reach rd32, %s to reaching sweet 16, %s to reach elite 8, %s to reach final four, %s to be runner up, and %s to win the ship " %(self.name, self.baiScore, self.pct1win, self.pct2win, self.pct3win, self.pct4win, self.pct5win, self.pct6win)




	##given the odds of reaching each round and the current size of the pot (or an estimate), determine a teams payout
	##uses expected value to determine payout based on the pot.
	def predict_payout(self, pot):
		return 1826/100 * self.baiScore


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
			while linetemp[2][0].isalpha():
				linetemp[1] = linetemp[1] + " " + linetemp[2]
				linetemp.pop(2)
			linetemp[1] = linetemp[1].lower()

			if linetemp[6][0] == '<' :
				linetemp[6] = linetemp[6][1:]
			if linetemp[7][0] == '<':
				linetemp[7] = linetemp[7][1:]

			oddsKenPom[linetemp[1]] = teamOdds(linetemp[1], linetemp[2], linetemp[3], linetemp[4], linetemp[5], linetemp[6], linetemp[7])


	#combine for each region
	#create new entries in dictionarys
def combine_lowseeds(dictionary):
	southsum = 0
	for x in LOWERSOUTH:
		southsum += dictionary[x].baiScore
		dictionary.pop(x)
	dictionary['south dogs'] = teamOdds('south dogs')
	dictionary['south dogs'].baiScore = southsum

	westsum = 0
	for x in LOWERWEST:
		westsum += dictionary[x].baiScore
		dictionary.pop(x)
	dictionary['west dogs'] = teamOdds('west dogs')
	dictionary['west dogs'].baiScore = westsum

	midwestsum = 0
	for x in LOWERMIDWEST:
		midwestsum += dictionary[x].baiScore
		dictionary.pop(x)
	dictionary['midwest dogs'] = teamOdds('midwest dogs')
	dictionary['midwest dogs'].baiScore = midwestsum

	eastsum = 0
	for x in LOWEREAST:
		eastsum += dictionary[x].baiScore
		dictionary.pop(x)
	dictionary['east dogs'] = teamOdds('east dogs')
	dictionary['east dogs'].baiScore = eastsum

def combine_elevens(dictionary):
	dictionary['eleven south'] = teamOdds('eleven south')
	dictionary['eleven south'].baiScore = dictionary['vanderbilt'].baiScore + dictionary['wichita st.'].baiScore
	dictionary.pop('vanderbilt')
	dictionary.pop('wichita st.')

	dictionary['eleven midwest'] = teamOdds('eleven midwest')
	dictionary['eleven midwest'].baiScore = dictionary['michigan'].baiScore + dictionary['tulsa'].baiScore
	dictionary.pop('michigan')
	dictionary.pop('tulsa')





read_KenPom()
pot = Pot()
combine_lowseeds(oddsKenPom)
combine_elevens(oddsKenPom)

# pot.estimate = 1000
# count = 0
# for x in oddsKenPom:
# 	count += oddsKenPom[x].predict_payout(pot)
# 	print x, oddsKenPom[x].predict_payout(pot)
# print 
# print count

print
print '~~~~~~~~~WELCOME TO THE ALPHA VERSION OF CALCUTTA BOT~~~~~~~~'
print
print 'the bot expects the auction to begin w/ the dogs and move to the lower seeds'
print '---please track all bids w/ the command "a *price*" like "a 5" to indicate a team sold for $5---'
print 'the pot estimation will update every 4 bids, or after eachof the 13 rounds'
print '---to check the value of a team based on the current estimate pot size use the command "t *team*"---'
print 'team must be all lower case. ie "t kansas" to get the current value of kansas'
print '---to assess the value of a team with a manual pot estimation, use the command "m *team* *estimate* ---'
print '---to quit please use the command "stop" ---'

print
print




# #testing
# print pot.get_value()
# print pot.get_estimate()

# pot.add_team(7)
# pot.add_team(10)
# pot.add_team(15)
# pot.add_team(20)

# print pot.get_estimate()
# #end testing

while 1:
	s = raw_input("enter a command:  ")
	if s == 'stop':
		break
	elif s[0] == 'a':
		pot.add_team(float(s[2:]))
		print '%i teams have been sold. The current pot value is %f' % (pot.num_teams(), pot.get_value())
	elif s[0] == 't':
		team = s[2:]
		print "based on the current estimated pot of %f, %s is expected to yield $%f" % (pot.get_estimate(), team, oddsKenPom[team].predict_payout(pot))
	# elif s[0] == 'm':
	# 	l = s.split()
	# 	est = 







