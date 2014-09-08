#!/usr/bin/python
blood = 100
attack = 50
hero = {'name':'milo','blood':100,'attack':50}
roomNum = [1,2,3,4,5,6,7,8,9,10]
def apple (blood):
	blood+=10
	return blood
def bomb (blood):
	blood-=10
	return blood
def knife (attack):
	attack+=10
	return attack

articleName = (apple(hero[blood]),bomb(hero[blood]),knife(hero[attack]))


    
for i in roomNum:
	random.choice(article)
	print hero & i
else:
	print "Game is completed"
	

  
	 
	
	
	


