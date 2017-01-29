
import string
import random

#all cards
list = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
#different suites
suite = ['S','H','C','D']
#face value of cards
facevalue = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#0 for cards with numbers or A, 1 for J,Q,K
face = [0,0,0,0,0,0,0,0,0,0,1,1,1]
#game value of cards
gamevalue = [14,2,3,4,5,6,7,8,9,10,11,12,13]

class Card:
	_card = ''	
	card_value = ''
	card_type = ''
	gamevalue = 0

	def __init__(self,card_value,card_type,gamevalue):
		self._card = ''+str(card_value)+str(card_type)
		self.card_value = card_value
		self.card_type = card_type
		self.gamevalue = int(gamevalue)

	def __repr__(self):
		return self._card
	def __str__(self):
		return self._card

def id_generator():
	s1 = ''.join(random.choice('123456789') for l1 in range(1))
	s2 = ''.join(random.choice(string.digits) for l2 in range(1))
	s3 = ''.join(random.choice(string.ascii_uppercase) for l3 in range(3))
	return s1 + s2 + s3

def player_generator():
	s1 = ''.join(random.choice('123456789') for l1 in range(1)) 
	s2 = ''.join(random.choice(string.digits) for _ in range(4))
	return s1 + s2
def gameid_generator(size=3):
	s = set()
	while len(s) < size:
		s.add(id_generator())
	return s;

def playerid_generator(size = 7):
	s = set()
	while len(s) < size:
		s.add(player_generator())
	return s;






gameSet = []
games = gameid_generator()
players = playerid_generator()

for v1 in suite:
	index = 0
	for v2 in list:
		newCard  = Card(v2,v1,gamevalue[index])
		gameSet.append(newCard)
		index = index + 1







def generatePokerHandsData():
	pokerHandsData = ''
	for game in games:
		random.shuffle(gameSet)
		tempCardSet = set(gameSet)
		# random.shuffle(tempCardSet);
		gamePlayers = random.sample(players, random.randrange(3,7,1))
		for player in gamePlayers:
			playerCards = [tempCardSet.pop(),tempCardSet.pop(),tempCardSet.pop(),tempCardSet.pop(),tempCardSet.pop()]
			playerCards.sort(key=lambda x: x.gamevalue, reverse=True)
			pokerHandsData = pokerHandsData + str('('+ str(player)  + ','+ str(game)  
					+ ','+ str(playerCards[0]._card) +','
					+ str(playerCards[1]._card) +','+str(playerCards[2]._card) +','+str(playerCards[3]._card) +','+
					str(playerCards[4]._card) +'),\n')

	return pokerHandsData	

def generatePokerCardsData():
	pokerCardsData = ''
	for v1 in suite:
		num = 0
		for v2 in list:
			pokerCardsData = pokerCardsData + str('('+ str(v2) + str(v1) + ',' + str(face[num])+ ',' 
				+ str(v2) + ','+str(v1) + ','+ str(facevalue[num]) +','
					+ str(gamevalue[num])+'),\n')
			num = num + 1
	return pokerCardsData

f = open('data.txt','w')
f.write('\n\nPoker Hands Data\n')
f.write(generatePokerHandsData())
f.write('\n\nPoker Cards Data\n')
f.write(generatePokerCardsData())
f.truncate()
f.close()