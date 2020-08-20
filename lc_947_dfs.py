class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        self.visited_set = set((i,j) for i,j in stones)
        self.row_dict, self.col_dict = collections.defaultdict(list), collections.defaultdict(list)
        for row, col in stones:
            self.row_dict[row].append(col)
            self.col_dict[col].append(row)
        count = 0
        for r,c in stones:
            if (r,c) in self.visited_set:
                self.connected_stones(r,c)
                count += 1

        return len(stones)-count


    def connected_stones(self, x,y):
        self.visited_set.discard((x,y))

        for c in self.row_dict[x]:
            if (x,c) in self.visited_set:
                self.connected_stones(x,c)


        for r in self.col_dict[y]:
            if (r,y) in self.visited_set:
                self.connected_stones(r,y)

        return