import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in xrange(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []

        
            
        
                

if __name__ == '__main__':
    find_order = Solution()
    find_order.findOrder(8,[[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]])



# 1st Approach
# if s[i] == '(':
    # push into the stack 
# elif s[i] == ')':
    # if my current is not empty
        # pop the topmost element from the stack
        # curr_str += s[i]
# else:
      # curr_str += s[i]

# final_str = ""
# for iter in curr_str:
    # if curr_str[i] == '(':
        # stack is not empty:
            # pop from the stack
            # continue
    # final_str += curr_str[i]

# Better Approach
# When do we term a string as invalid?
# ) ( # count = 0
# count -= 1, if count < 0 -> remove. (reset the count.)
# count -=2, if count < 0 -> remove again. (reset the count.) # count = 0
# now, what we will have is -> count = 1, count = 2
# count = 1, count = 2 
# if count = 0 -> break or else keep removing until you find one. iterating backwards ?



# (l(a(b)c)d

[0]
   *   *   *
[0,1,(,3,(,5,),6,),d]
"".join(ret)

# Binary order traversal
# Merge k sorted list
# Numner of islands
# Number of distinct isalnds
# DFS with memoizattion
# 




