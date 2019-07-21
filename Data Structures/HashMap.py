'''
Hash Map
Page 99 To explain the importance of understanding arrays
A HashMap takes a value (often a string) and computes a 'hash' 
the hash is normally an int or long
the hash is then made to fit within an array length
normally through the use of modulo

example:

Input : Key = "cAt" |  Value = "calico"
Hash:
	c = 2
	A = 27
	t = 20
   +  -----
   hash = 49
  
  ----------------
  |  |  |  |  |  |
  ----------------  n = 5
  
  49 % 5 = 4
  
  ---------------------
  |  |  |  |  |"calico"|
  ---------------------
  
 Then to return to the same spot the 
 hash algorithm is repeated to find the index
 
 To fix collisions:
	*increment hashed index and increase hashmap size when full
	*have each hash index store a linked list of values that hashed
		to the same key
		
		
'''


class YoungHashMap (object):
	def __init__(self,n):
		self.n = n
		self.hashmap = [[]]*n
	
	def Insert(self,key,value):
		ha = hash(key)
		index = ha % self.n
		self.hashmap[index].append((key,value))
	
	def __getitem__(self,key):
		ha = hash(key)
		index = ha % self.n
		for k , v in self.hashmap[index]:
			if k == key:
				return v
		

if __name__ == "__main__":
	yhm = YoungHashMap(100)
	yhm.Insert(25, "Hello")
	yhm.Insert("hello", 30)
	yhm.Insert("bye","good")
	print(yhm["bye"])
	print(yhm["hello"])
	print(yhm[25])
		
	
	
	
	
	
	
	
	
	
	