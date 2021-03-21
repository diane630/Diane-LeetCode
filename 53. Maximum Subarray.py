class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # pathsum = [0 for i in range(len(nums))] 
        # # from index 0 to index i inclusive
        # pathsum[0] = nums[0]
        # for i in range(len(nums)):
        #     pathsum[i] = pathsum[i-1] + nums[i]
        # largest_sum = float('-inf')
        
        # dp[j] = (sum) largest subarry sum with range enmding j
        # if pathsum (i, j) > 0 don't change i 
        # else i = j
        
        # dp[j] = maxsubatrray sum with ending index at j
        # if dp[j] =0 when it's always good not to include j (e.g. nums[j] = -99999999)
        dp = [0 for j in range(len(nums))]
        if nums[0] > 0:
            dp[0] = nums[0]
        for j in range(1, len(nums)):
            if dp[j-1] + nums[j] > 0:
                dp[j] = dp[j-1] + nums[j]
        
        if max(dp) > 0:
            return max(dp)
        return max(nums)