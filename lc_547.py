class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.disjoint_comp = [i for i in range(0, len(M))]
        for i in range(0, len(M)):
            for j in range(i+1, len(M[0])):
                if M[i][j]:
                    self.union(i,j)
                        
        circles = set(self.find(i) for i in range(len(M)))  
        return len(circles)
    
    def union(self,x,y):
        mx = self.find(x)
        my = self.find(y)
        self.disjoint_comp[my] = mx
        
    def find(self, x):
        if self.disjoint_comp[x] == x:
            return x
        self.disjoint_comp[x] = self.find(self.disjoint_comp[x]) # path compression
        return self.disjoint_comp[x]