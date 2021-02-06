class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dict_bracketpairs = {'(' : ')', '[' : ']', '{' : '}'}
        i = 0
        while i < len(s):
            strlist = list(s)
            if strlist[i] in dict_bracketpairs:
                stack.append(strlist[i])
            else:
                if not stack:
                    return False
                if dict_bracketpairs[stack.pop()] == strlist[i]:
                    pass
                else:
                    return False
            i += 1
        if stack:
            return False
        return True