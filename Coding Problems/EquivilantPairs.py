'''
Page 79 Finding Solutions to a^3+b^3=c^3+d^3 where a,b,c,d are integers 1-1000
This solution represents the benefits of
reducing unnecessary work

Instead of computing each variable 
1-1000 and checking each time if a^3+b^3=c^3+d^3
this would take O(N^4) where n = 1000

What we do to reduce unnecessary work is to compute 
i^3 + j^3 for all pairs of integers i,j between 1-1000
and store these pairs in a list at a spot in a hash table 
with the key being the result of the equation

With this hash table at each key will be the 
values which solve a^3+b^3=c^3+d^3 

Just print out each pair of pairs from this list

'''

solutions = {}
for i in range(1,1000):
	for j in range(1,1000):
		result = i**3+j**3
		if result not in solutions.keys():
			solutions[result] = [(i,j)]
		else: 
			solutions[result].append((i,j))
			
for results in solutions.keys():
	pairlist = solutions[results]
	for i in range(0,len(pairlist)):
		for j in range(i+1,len(pairlist)):
			print(str(pairlist[i][0]) + "^3 + " + str(pairlist[i][1]) + "^3 = " + \
					str(pairlist[j][0]) + "^3 + " + str(pairlist[j][1]) + "^3 = " + \
					str(results))
	