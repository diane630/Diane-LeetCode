# 4. Median of Two Sorted Arrays
# Hard

# 8942

# 1373

# Add to List

# Share
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        if (m + n) % 2 == 1:
            k = (m + n)//2
            med = self.find_k(nums1, nums2, k)
            #print(med)
            
        else:
            k1 = (m + n - 1)//2
            k2 = (m + n)//2
            med1 = self.find_k(nums1, nums2, k1)
            med2 = self.find_k(nums1, nums2, k2)
            med = (med1+ med2)/2
        
        return float(med)
        
    def find_k(self, nums1:List[int], nums2:List[int], k:int) -> int:
        #在nums1, nums2的整合array中找到idx = k 的数
        if not nums1:
            #print('nums1 空', nums1,nums2)
            return nums2[k]
            
        if not nums2:
            #print('nums2 空', nums1,nums2)
            return nums1[k]      
            
        if not k:
            #print('k=0', nums1,nums2)
            return min(nums1[0], nums2[0])
            
        pivot_idx = min(len(nums1)-1, len(nums2)-1, (k-1)//2)
        pivot_1 = nums1[pivot_idx]
        pivot_2 = nums2[pivot_idx]
        if pivot_1 <= pivot_2:
            #舍去nums1,pivot_1以及以前的部分
            return self.find_k(nums1[pivot_idx+1:], nums2, k-pivot_idx-1)
            #return x if x else None
        else:
            #舍去nums2,pivot_2以及以前的部分
            return self.find_k(nums1, nums2[pivot_idx+1:], k-pivot_idx-1)
            #return x if x else None