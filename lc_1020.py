class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        count = 0
        direction = [(-1,0),(0,1),(0,-1),(1,0)]
        for i in range(1,m-1):
        	for j in range(1, n-1):

        		if A[i][j] == 1:
        			walk_poss, ones = self.find_connected_components(A, direction, i,j, m,n)
        			if not walk_poss:
        				count += ones

        return count

    def find_connected_components(self, matrix, directions,  x,y, m, n):
        import pdb
        pdb.set_trace()
        result = False
        count = 0

        if (x == 0 or x == m-1) and (y == 0 or y == n-1):
            if matrix[x][y] == 1:
                return (True,count)
            else:
                return (False,count)

        if matrix[x][y] == 0:
            return (False,count)

        if matrix[x][y] == 1:
            count += 1
            matrix[x][y] == 0

        for move in directions:
            move_x = x + move[0]
            move_y = y + move[1]
            is_boundary, one_count = self.find_connected_components(matrix, directions, move_x, move_y, m, n)
            count += one_count
            if is_boundary:
                result = True

        return (result, count)

if __name__ == '__main__':
    find_order = Solution()
    find_order.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])



'''
[[0,1,1,0],
 [0,0,1,0],
 [0,0,1,0],
 [0,0,0,0]]
'''
