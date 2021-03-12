class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {}
        # def dp(amount):
        #     if amount == 0:
        #         return 0
        #     if amount < 0:
        #         return float('inf')
        #     if not amount in memo:
        #         memo[amount] = 1 + min(dp(amount - coin) for coin in coins)
        #     return memo[amount]
        # ret = dp(amount)
        # return ret if ret < float('inf') else -1
        
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        #print(dp)
        return dp[-1] if dp[-1] < float('inf') else -1