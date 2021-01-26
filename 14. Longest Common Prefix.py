# 14. Longest Common Prefix
# Easy

# 3584

# 2098

# Add to List

# Share
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

Class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if all(strs) == False:
            return ""
        k = 99999999
        for s in strs:
            if len(s) < k:
                k = len(s)
        temp = strs[0]
        i = 0
        while True:
            for s in strs:
                if i == k or s[i] != temp[i]:
                    return temp[0:i]
            i += 1
                
          
