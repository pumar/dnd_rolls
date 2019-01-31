from random import randint
import matplotlib.pyplot as plt
import numpy as np

n = 100000
sum_score = 70

abscore_tot = []


def rolls():
	roll = []
	for i in range(0,4):
		roll.append(randint(1,6))
	roll.sort()
	return roll

for i in range(0,n):
	stat_sum = []
	for j in range(0,6):
		r = rolls()
		stat_sum.append(sum(r[1:]))
	abscore_tot.append(sum(stat_sum))


hist, bin_edges = np.histogram(abscore_tot,bins = range(min(abscore_tot),max(abscore_tot)))
hist = [float(i)/float(sum(hist)) for i in hist]

for i in range(len(hist)):
	print( str(hist[i]) + ',' + str(bin_edges[i]))

#rint( str((sum(hist[np.where( (bin_edges[:-1]>= sum_score) & (bin_edges[:-1]<=sum_score+10) )])/float(n))*100)+'%' )


"""
plt.figure()
plt.hist(x = abscore_tot, bins = range(min(abscore_tot),max(abscore_tot)))
plt.savefig('/home/caiopumar/Documents/statdist.png')
plt.close()
"""