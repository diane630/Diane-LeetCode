class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violation = 0
        i = 1
        while i < len(nums):
            if violation > 1:
                return False
            if nums[i] >= nums[i-1]:
                i += 1
                continue
            else:
                if i == len(nums)-1:
                    return violation < 1
                elif i == 1:
                    nums[0] = float('-inf')
                    violation += 1
                    i += 1
                elif nums[i+1] >= nums[i-1]:
                    nums[i] = float('-inf')
                    violation += 1
                    i = i + 1
                elif nums[i] >= nums[i-2]:
                    nums[i-1] = float('-inf')
                    violation += 1
                    i = i + 1
                else:
                    return False
        #print(nums)
        return True