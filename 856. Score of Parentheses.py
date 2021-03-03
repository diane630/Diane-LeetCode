class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        res = 0
        for p in S:
            if p == "(":
                stack.append(0)
            elif p == ")":
                accum_val = stack.pop()
                process_val = max(1, 2*accum_val)
                if not stack:
                    res += process_val
                    continue
                stack[-1] += process_val
                
        return res
        