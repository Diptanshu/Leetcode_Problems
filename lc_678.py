
# Brute Force
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        def validate_string(i, open_count):
        	if i == n:
        		return open_count == 0:
      
        	if s[i] == '(':
        		return validate_string(i+1, open_count+1)
        	elif s[i] == ')':
        		return open_count != 0 and validate_string(i+1, open_count-1)
        	else:
        		return validate_string(i+1, open_count) ||
        			   validate_string(i+1, open_count+1) ||
        			   open_count != 0 and validate_string(i+1, open_count-1)

# Memoized Solution

class Solution(object):
    def checkValidString(self, s):
    	mem_cache = {}

   	def validate_string(i, open_count):
   		if i == n:
   			return open_count == 0
   			

   		if (index, open_count) in mem_cache:
   			return mem_cache[(index, open_count)]
      
       	if s[i] == '(':
       		mem_cache[(index,open_count)] = validate_string(i+1, open_count+1)
        elif s[i] == ')':
        	mem_cache[(index,open_count)] = open_count != 0 and validate_string(i+1, open_count-1)
        	else:
        		mem_cache[(index,open_count)] = validate_string(i+1, open_count) ||
        			   validate_string(i+1, open_count+1) ||
        			   open_count != 0 and validate_string(i+1, open_count-1)

        return mem_cache[(index, open_count)]

# Greedy Algorithm

def checkValidString(self, s):
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0










