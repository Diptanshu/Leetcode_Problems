class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [float("inf") for i in range(0, 366)]
        dp[0] = day_index = 0
        for day in range(1, 366):
            if  day_index < len(days) and days[day_index] == day:
                for idx, sub_days in enumerate([1,7,30]):
                    dp[day] = min(dp[day], dp[max(0,day - sub_days)] + costs[idx])
                day_index += 1    
            else:
                dp[day] = dp[day-1]
        
        print (dp)
        return dp[-1]
                

if __name__ == '__main__':
    solution = Solution()
    solution.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15])
                