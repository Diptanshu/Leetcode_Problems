class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # No duplicate edges.
        # Approach 1 dfs with recursion 
        # - visited array maintaining a list of courses
        # - maintain a adjaceny list of edges
        # - detecting cycles.
        # - base case in dfs
        # - there could be two different connected components.
        # - Ultimately there needs to be a node that doesnt have any outward edges.
        
        
        # check for cycles in DFS
        # marked a vertex as true / false
        
        
        self.outdegree = collections.defaultdict(list)
        for i,j in prerequisites:
            self.outdegree[i].append(j)
            
            
        self.ans = []
        self.visited = [0] * numCourses
        self.found_cycle = 0
        for i in range(0, numCourses):
            if self.found_cycle == 1:
                break
            if not self.visited[i]:
                self.dfs(i)
        
        return [] if self.found_cycle == 1 else self.ans
                
        
    def dfs(self, start):
        if self.found_cycle == 1:
            return 
        
        if self.visited[start] == 1:
            self.found_cycle = 1
            return
        
        if self.visited[start] == 0:
            self.visited[start] = 1
            for neigh in self.outdegree[start]:
                self.dfs(neigh)
            
            self.visited[start] = 2
            self.ans.append(start)
        
