# 电话号码（输入一个map（数字 -> char list）和 数字string， 输出所有组合）
# follow-up：多个数字 比如 ”1234“ 可以是 ”1｜23｜4“， 或者”1｜234｜“， 或者”12｜34“， etc。所有的combination
# follow-up：优化。我用的反序数字+记忆

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:

        
#         phone = {'2': ['a','b','c'],'3': ['d','e','f'],\
#                 '4': ['g','h','i'],'5': ['j','k','l'],\
#                 '6': ['m','n','o'],'7': ['p','q','r','s'],\
#                 '8': ['t','u','v'],'9': ['w','x','y','z']}
        
#         def backtrack(combination, next_digits):
#             if len(next_digits) == 0:
#                 output.append(combination)
#             else:
#                 for letter in phone [next_digits[0]]:
#                     backtrack(combination + letter, next_digits[1:])
        
#         output =[]
        
#         if digits:
#             backtrack("", digits)
#         return output

class Solution:
    def partition(self, digits):
        # all possible partition
        if not digits:
            return [[]]
        if len(digits) == 1:
            return [[digits]]
        ret = []
        for i in range(1, len(digits)+1):
            left = [digits[:i]]
            rights = self.partition(digits[i:])
            # print(left, rights)
            for right in rights:
            	complete = left + right
            	# print(complete)
            	ret.append(complete)
        return ret

    def decode(self, digits):
        def backtrack(remains, path):
            if not remains:
                self.ret.append("".join(path))
                return
            first = remains[0]
            if not first in self.num_map:
                return
            for letter in self.num_map[first]:
                path.append(letter)
                backtrack(remains[1:], path)
                path.pop()
        backtrack(digits, [])
        # return self.ret
    
    def digits_to_letters(self, digits, num_map):
        self.ret = []
        self.num_map = num_map
        combinations = self.partition(digits)
        print(combinations)
        for comb in combinations:
            self.decode(comb)
        return self.ret


a = Solution()
digits = "23"
phone = {'2': ['a','b','c'],'3': ['d','e','f'],\
        '4': ['g','h','i'],'5': ['j','k','l'],\
        '6': ['m','n','o'],'7': ['p','q','r','s'],\
        '8': ['t','u','v'],'9': ['w','x','y','z'],
        "23":["23"]}
ans = a.digits_to_letters(digits, phone)
# pat = a.partition(digits)
print(ans)
