# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_non_repeat = set()
    
        
        temp = ""
        res = ""
        lenres = 0
        for let in s:
            if let not in set_non_repeat:
                set_non_repeat.add(let)
                temp += let
                # amintain res and lenres
                if len(temp) >= lenres:
                    res = temp
                    lenres = len(res)
            else:
                ind = temp.index(let)
                # maintain set
                for char_before_repoeated_let in temp[:ind]:
                    set_non_repeat.remove(char_before_repoeated_let)
                # amintain res and lenres
                if len(temp) >= lenres:
                    res = temp
                    lenres = len(res)
                #maintain temp
                temp = temp[(ind + 1):] + let
        return len(temp) if res == "" else len(res)
                
                