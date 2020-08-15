import math
class Solution(object):
    def knightDialer(self, N):
        # Solution not Working
        m = 4 
        n = 3
        dp_table = []
        mod_max = int(math.pow(10,9)) + 7
        for hops in range(0,N+1):
            temp_dp_table = []
            for row in range(0,m):
                temp_list = []
                for col in range(0,n):
                    temp_list.append(0)
                temp_dp_table.append(temp_list)
            dp_table.append(temp_dp_table)
        
        unique_nums = 0

        import pdb
        pdb.set_trace()
        for i in range(0,4):
            for j in range(0,3):

                unique_nums += (unique_nums + self.unique_paths(dp_table, N, i,j))%mod_max
                print (unique_nums)
        return int(unique_nums)
    
    def unique_paths(self, dp_table, n, i, j, mod_max=int(math.pow(10,9)) + 7):
        if (i < 0 or i > 3 or j < 0 or j > 2 or (i == 3 and j == 0) or (i == 3 and j ==  2)):
            return 0
        if n == 1:
            return 1
        if dp_table[n][i][j]:
            return dp_table[n][i][j]
        dp_table[n][i][j] = self.unique_paths(dp_table,n-1, i-2,j-1)%mod_max + \
                            self.unique_paths(dp_table,n-1, i-1,j-2)%mod_max + \
                            self.unique_paths(dp_table,n-1, i+1,j-2)%mod_max + \
                            self.unique_paths(dp_table,n-1, i+2,j-1)%mod_max + \
                            self.unique_paths(dp_table,n-1, i-2,j+1)%mod_max + \
                            self.unique_paths(dp_table,n-1, i-1,j+2)%mod_max + \
                            self.unique_paths(dp_table,n-1, i+1,j+2)%mod_max + \
                            self.unique_paths(dp_table,n-1, i+2,j+1)%mod_max
        return dp_table[n][i][j]

if __name__ == '__main__':
    soln = Solution()
    soln.knightDialer(1)