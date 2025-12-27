class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0 
        minbuy = prices[0]
        for p in prices : 
            minbuy = min (minbuy,p)
            profit = max(profit,  p - minbuy )
        return profit 
        