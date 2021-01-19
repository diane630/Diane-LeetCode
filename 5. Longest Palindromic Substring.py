# 5. Longest Palindromic Substring
# Medium

# 9283

# 626

# Add to List

# Share
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        
        n = len(s)
        
        ans = ''
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            
        maxLen = 1
        for i in range(n-1):
            j = i + 1
            dp[i][j] = s[i] == s[j]
            if dp[i][j] and (2 > maxLen):
                maxLen = 2
                ans = s[i:j+1]
        
        
        for _ in range(n-2):
            i = 0
            j = i + 2
            while (i < n ) and (j < n):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j] and (j - i +1 > maxLen):
                    maxLen = j - i + 1
                    ans = s[i: j +1]
                i += 1
                j += 1
            
        return ans