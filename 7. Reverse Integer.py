# 7. Reverse Integer
# Easy

# 4223

# 6536

# Add to List

# Share
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0

class Solution:
    def reverse(self, x: int) -> int:
        intmax = 2 **31 -1
        rev = 0
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        
        while x != 0:
            pop = x % 10
            x = x // 10
            
            #if overflow
            if rev > intmax//10:
                return 0
            if rev == intmax//10:
                if sign == 1 and pop > 7: 
                    return 0
                if sign == -1 and pop > 8:
                    return 0       
            
            rev = rev * 10 + pop
        return rev * sign