class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        memo = {}
        mod = 10**9 + 7
        m = len(pizza)
        n = len(pizza[0])
        
        # region sum from [r, c] to [m-1, n-1] inclusive
        # dummy row, col at row = m and col = n
        suffix_sum = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                suffix_sum[r][c] = suffix_sum[r + 1][c] + suffix_sum[r][c + 1] - suffix_sum[r + 1][c + 1] + (pizza[r][c] == 'A')
        
        def has_apple(r1, c1, r2, c2):
            # return apple num in region (r1, c1), (r2, c2) inclusive
            # r1 <= r2
            # c1 <= c2
            return suffix_sum[r1][c1] - suffix_sum[r2 + 1][c1] - suffix_sum[r1][c2 + 1] + suffix_sum[r2 + 1][c2 + 1]
            
        
        def dp_helper(rest_k, r, c) -> int:
            if rest_k <= 0:
                if has_apple(r, c, m - 1, n - 1) > 0:
                    return 1
                else:
                    return 0
            way = 0
            if not tuple([rest_k, r, c]) in memo:
                # cut horizontally
                for cut_r in range(r + 1, m):
                    increm = 0
                    if has_apple(r, c, cut_r - 1, n - 1) > 0:
                        increm = dp_helper(rest_k - 1, cut_r, c)
                    way = (way + increm) % mod
                # cut vertically
                for cut_c in range(c + 1, n):
                    increm = 0
                    if has_apple(r, c, m - 1, cut_c - 1) > 0:
                        increm = dp_helper(rest_k - 1, r, cut_c)
                    way = (way + increm) % mod
                memo[tuple([rest_k, r, c])] = way
            return memo[tuple([rest_k, r, c])]
                
        return dp_helper(k - 1, 0, 0)