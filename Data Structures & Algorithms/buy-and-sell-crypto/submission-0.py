class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 999
        max_profit = 0
        for day, price in enumerate(prices):
            # if we find a new min price, selling options start next day, else is skipped for this iter
            if price < min_price:
                min_price = price
                # min_day = day
                # print(f"min_price found: {min_price}, {day}")
            else:
                profit = price - min_price
                # print(f"min_price/day = {min_price}/{min_day}")
                # print(f"sell price/ day/ profit = {price}/{day}/{profit}")
                max_profit = max(max_profit, profit)

        return max_profit 