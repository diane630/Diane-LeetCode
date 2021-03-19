class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        ans = []
        counters = dict()
        i = 0
        for word in arr:
            counter = [0 for i in range(26)]
            for char in word:
                counter[ord(char) - ord('a')] += 1
            counter = tuple(counter)
            if not counter in counters:
                ans.append([])
                counters[counter] = i
                i += 1
            ans[counters[counter]].append(word)
        return ans