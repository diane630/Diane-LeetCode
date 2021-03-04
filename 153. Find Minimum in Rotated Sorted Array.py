class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        if not nums:
            return -1
        
        if len(nums) <= 1:
            return nums[0]
        
        while l <= r:
            mid = (r - l) // 2 + l
            # l = 0, r = 1
            if mid == 0:
                return nums[l] if nums[mid] < nums[mid+1] else nums[r]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[len(nums)-1]:
                r = mid - 1
            else:
                l = mid + 1
        