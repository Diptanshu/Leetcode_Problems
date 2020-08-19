#Union find is basically building a forest of trees out of a graph.
#For typical inputs, the trees will have a height of log(N),
#which results in log(N) array look-ups for each of the N nodes
#in the graph, hence, O(Nlog(N))

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        self.sto_comp = [i for i in range(0,19999)]
        self.totals = [0 for i in range(0,19999)]
        for r,c in stones:
            self.union(r, c+10000)
            self.totals[self.find(r)] += 1
        
        count = 0
        for idx, total in enumerate(self.totals):
            if total > 0:
                count += total-1
        return count
    
    def union(self, mx, my):
        x = self.find(mx) # 2
        y = self.find(my) # 1
        if x != y:
            self.sto_comp[y] = x
            self.totals[x] += self.totals[y]
            self.totals[y] = 0
    
    def find(self, x):
        if self.sto_comp[x] == x:
            return x 
        self.sto_comp[x] = self.find(self.sto_comp[x])
        return self.sto_comp[x]