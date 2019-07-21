'''
Page 86 To describe Best Conceivable Runtime
To find all the pairs in two sorted lists
and to achieve O(N) without any additional space
one must only do a linear search
where each iteration starts at the index
where the previous pair was found
'''

A = [13,27,35,40,49,55,59,70,89,100]
B = [17,35,39,40,55,58,60,70,89,90,91,92,95,100]
n = len(A) + len(B)
Pairs = []
i = 0
j = 0
iters = 0
while (i < len(A)) and (j < len(B)):
	iters += 1
	if (A[i] > B[j]):
		j += 1
	elif (A[i] < B[j]):
		i += 1
	else:
		Pairs.append(A[i])
		i += 1
		j += 1

print(Pairs)
print("Iterations = {} | N = {}".format(iters,n))