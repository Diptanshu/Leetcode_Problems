# Approach 1 #
# learning - rolling hash
# edgecase study - odd and even length strings 

class Solution:
	def longestDecomposition(self, text: str) -> int:
		# Approach 3 
		# dp 






		
		'''
		# Approach 2 
		# Memoization 
		# ghiabcdefhelloadamhelloabcdefghi"
		self.mem_cache = {}
		def find_chunks(i, j):
			if i == j:
				return 1
			if (i,j) in self.mem_cache:
				return self.mem_cache[(i,j)]
			k = 0
			ans = 1
			while (i+k <= j-k):
				if (text[i:i+k+1] == text[j-k:j+1]):
					ans = max(ans, 2 + find_chunks(i+k+1, j-k-1))
				k += 1
			self.mem_cache[(i,j)] = ans
			return self.mem_cache[(i,j)]
			print (self.mem_cache)
		return find_chunks(0,len(text)-1)
		'''
		'''
		# Approach 1 
		# Rolling Hashes 
		low = 0
		high = len(text)-1
		low_hash = high_hash = curr_hash_length = chunks = 0
		magic_prime = 32416189573
		while (low < high):
			low_hash = low_hash * 26
			low_hash += ord(text[low]) - ord('a')
			high_hash = high_hash + (ord(text[high])-ord('a')) * pow(26,curr_hash_length, magic_prime)
			low_hash = low_hash%magic_prime
			high_hash = high_hash%magic_prime
			curr_hash_length += 1
			if low_hash == high_hash:
				curr_hash_length = low_hash = high_hash = 0
				chunks += 2
			low += 1
			high -= 1
		if (low == high and curr_hash_length == 0) or curr_hash_length > 0:
			chunks += 1
		return chunks
		'''





if __name__ == "__main__":
	soln = Solution()
	chunks_count = soln.longestDecomposition("aaa")
	print (chunks_count)






'''

Approach 2 

Brute Force:

# ab| merchant |ab
# ab s |   | s ab
	   +1 -1 

# ab| def def| ab

# - i = 2; j = 7

	[2:3]	[7:8]

if i <= j:
	return 1


some k reduction that I am doing.

k = 0

abab

s[0:2] == s[2:4]

def find_chunks(i, j):

	ans = 1
	while (i+k <= j-k):
		if (str[i:i+k+1] == str[j-k:j+1]):
			ans = max(ans, 2 + find_chunks(i+k+1, j-k-1))
		k+= 1
	self.memo_dict[(i,j)] = ans
	return self.memo_dict[(i,j)]



Two parameters are there:
f(i, j) : {f(),f()} 

- if there is match
	- recurse with remaining parameters 
- else keep trying







class Solution:
    def longestDecomposition(self, text: str) -> int:
        self.memo = {}
        def dp(i,j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i,j) not in self.memo:
                k = 0
                tmp = 1
                while i+k< j-k:
                    if text[i:i+k+1] == text[j-k:j+1]:
                        tmp = max(tmp,2+dp(i+k+1,j-k-1))
                    k += 1
                self.memo[(i,j)] = tmp
            return self.memo[(i,j)]
        return dp(0,len(text)-1)

'''
