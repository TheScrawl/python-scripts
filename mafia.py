import random

playerList = []
mafiaCount = 0
roleList = ['doctor', 'detective']

#Get Extra Roles
moreRoles = input('extra roles? y/n ')
if moreRoles.lower() == 'y':
	newRole = None
	while newRole != 'z':
		newRole = input('Input Extra Roles. Type z to finish: ')
		if newRole != 'z':
			roleList.append(str(newRole))
			print('\nRole List')
			for i in roleList:
				print(i)
		else:
			break

#Get Player List
player= None
while str(player) != 'z':
	player= input('Input Players. Type z to finish: ')
	if player!= 'z':	
		playerList.append(str(player))
		print('\nPlayer List')
		for i in playerList:
			print(i)
	else:
		break

chosenPlayers = []
try:
	#Get Mafias
	mafiaCount = int(input('Number of Mafias: '))
	for i in range(mafiaCount):
		avaliablePlayers = [x for x in playerList if x not in chosenPlayers] 
		playerChoice = avaliablePlayers[random.randint(0, len(avaliablePlayers) - 1)]
		print(playerChoice  + ' is mafia')
		chosenPlayers.append(playerChoice)
	#Get Other Roles
	for i in roleList:	
		avaliablePlayers = [x for x in playerList if x not in chosenPlayers] 
		playerChoice= avaliablePlayers[random.randint(0, len(avaliablePlayers) - 1)]
		print(playerChoice + ' is ' + i)
		chosenPlayers.append(playerChoice)
	#Get Villagers	
	print('Rest are Villagers')
except (ValueError, IndexError):
	print('too many roles, not enough players')

		
