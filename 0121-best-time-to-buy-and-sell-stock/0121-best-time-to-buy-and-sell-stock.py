class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profitM = 0
        cost , sell = 0,1
        while sell < len(prices):
            if prices[cost] < prices[sell]:
                profit = prices[sell] - prices[cost]
                profitM = max(profit, profitM)
            else:
                cost = sell
            sell +=1
        return profitM


        # below this are all my useless tries

        # profit = 0
        # cost, sell = prices[0], prices[1]
        # for i in range(len(prices)-1):
        #     if sell < cost:
        #         cost, sell = prices[i], prices[i+1]
        #     else:
        #         if sell - cost > profit:
        #             profit = sell - cost
        #         sell = prices[i+1]
        # return profit




        # profit = 0
        # for i in prices:
        #     for j in range(prices.index(i), len(prices)):
        #         if prices[j] - i > profit:
        #             profit = prices[j] - i
        # return profit


        # cost = min(prices)
        # profit = -1
        # for i in range(prices.index(cost) , len(prices)):
        #     if prices[i]-cost > profit:
        #         profit = prices[i] - cost
        # return profit


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna