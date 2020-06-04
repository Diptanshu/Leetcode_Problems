class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # check null
        if len(prices) == 0:
            return 0
        
        s0 = [0 for i in range(len(prices))]
        sell = [0 for i in range(len(prices))]
        buy = [0 for i in range(len(prices))]
        
        buy[0] = -prices[0]
        s0[0] = sell[0] = 0
        
        for i in range(1,len(prices)):
            s0[i] = max(s0[i-1], sell[i-1])
            buy[i] = max(buy[i-1], s0[i-1] - prices[i])
            sell[i] = buy[i-1] + prices[i]
        
        return max(s0[i], sell[i])
