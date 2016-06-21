class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        left = [0] * (len(prices)+1)
        right = [0] * (len(prices)+1)
        min_price = prices[0]
        max_price = prices[len(prices)-1]
        max_profit = 0
        for i in range(1, len(prices)):
            left[i] = max(left[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        for i in range(len(prices)-1, -1, -1):
            right[i] = max(right[i+1], max_price - prices[i])
            max_price = max(max_price, prices[i])
        for i in range(0, len(prices)):
            max_profit = max(max_profit, left[i]+right[i+1])
        return max_profit