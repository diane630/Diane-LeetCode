class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        if not nums:
            return []
        self.dfs_helper(set(nums), [])
        return self.res
    def dfs_helper(self, unused: set[int], path: list[int]):
        if not unused:
            # append copy of path, not the address of path
            self.res.append(path[:])
            return
        for next_one in list(unused):
            unused.remove(next_one)
            path.append(next_one)
            self.dfs_helper(unused, path)
            path.pop()
            unused.add(next_one)
        
        