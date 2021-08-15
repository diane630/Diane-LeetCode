# Goldman sachs OA
class Solution:
    def maxSubArrayLen(arr, target):
        l, r = 0, 0
        max_length = 0
        sum_ = 0 # inclusive
        while r < len(arr):
            sum_ += arr[r]
            if sum_ < target:
                r += 1
                continue
            while l < len(arr) and sum_ - arr[l] > target:
                sum_ -= arr[l] 
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

                
            