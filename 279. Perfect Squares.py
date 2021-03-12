class Solution:
    def numSquares(self, n: int) -> int:
#         memo = {}
#         memo[0] = 0
#         def dp(n:int) -> int:
#             if n < 0:
#                 return float('inf')
#             if n not in memo:
#                 remaining_steps = float('inf')
#                 for base_num in range(1, int(n**0.5)+1):
#                     remaining_steps = min(remaining_steps, dp(n - base_num**2))
#                 memo[n] = remaining_steps + 1
#                 # print(memo)
#             return memo[n]
#         return dp(n)

        square_nums = [i **2 for i in range(0, int(n**0.5)+1)]
        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for sqaure in square_nums:
                if i < sqaure:
                    break
                dp[i] = min(dp[i], dp[i-sqaure] + 1)
        return dp[-1]
        