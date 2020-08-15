# Time complexity deeper analysis.

class Solution(object):
    def __init__(self):
        self.union_arr = [i for i in range(0,10001*2)]
        self.rank_arr = [0 for i in range(0,10001*2)]
    
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        for stone in stones:
        	r = stone[0]
        	c = stone[1] + 10001
        	self.makeSet(r,c)
            self.rank_arr[self.find_parent(r)] += 1

        remove_stones = 0
        for total in self.rank_arr:
        	if total > 0:
        		remove_stones += total-1

        return remove_stones

    def makeSet(self, r,c):
    	tx = self.find_parent(r)
    	ty = self.find_parent(c)
    	if tx != ty:
            self.union_arr[tx] = ty
    		self.rank_arr[ty] += self.rank_arr[tx] 
    		self.rank_arr[tx] = 0


    def find_parent(self,  index):
    	if self.union_arr[index] == index:
    		return index
    	self.union_arr[index] = self.find_parent(self.union_arr[index]) # path compression
    	return self.union_arr[index]



if __name__ == '__main__':
    final_soln = Solution()
    final_soln.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
