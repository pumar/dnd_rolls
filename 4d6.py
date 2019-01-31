from random import randint

def rolls():
	roll = []
	for i in range(0,4):
		roll.append(randint(1,6))
	roll.sort()
	return roll


for j in range(0,6):
	r = rolls()
	print('Rolls:  '+str(r)+',  Final Result: '+str(sum(r[1:])))
