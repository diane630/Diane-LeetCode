class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         tree_map_down: record edge going down only. ie: parent -> child
#         tree_map_up: record edge going up only. ie: child -> parent
#         has_apple_in_desc: record whether apple exists in chilren
#         works fine with tree structure, but not undirected graph
#         tree_map_down = collections.defaultdict(list)
#         tree_map_up = collections.defaultdict(list)
#         has_apple_in_desc = [False for i in range(n)]
        
#         def mark_parent_as_T(c_node):
#             for parent in tree_map_up[c_node]:
#                 if not has_apple_in_desc[parent]:
#                     has_apple_in_desc[parent] = True
#                     mark_parent_as_T(parent)
        
#         for edge in edges:
#             p, c = edge
#             tree_map_down[p].append(c)
#             tree_map_up[c].append(p)
            
#         for i, boolean in enumerate(hasApple):
#             if boolean == True:
#                 has_apple_in_desc[i] = True
#                 mark_parent_as_T(i)
        
#         def helper(p_node) -> int:
#             if not has_apple_in_desc[p_node]:
#                 return 0
#             ret = 0
#             for child in tree_map_down[p_node]:
#                 if has_apple_in_desc[child]:
#                     ret += (helper(child) + 2)
#             return ret
        
#         return helper(0)
        
        adj_map = collections.defaultdict(list)
        for v1, v2 in edges:
            adj_map[v1].append(v2)
            adj_map[v2].append(v1)
        visited = set()
        def helper(root: int) -> int:
            # return seconds starting from root plus two seconds on the incoming edges
            # if the sum of descedents is nonzero, return sum (don't care about whether apples present or not on this root)
            # if itself has no apple and sum of descedents is zero, return zero (implys don't go this way)
            # if itself has an apple and sum of descedents is zero, return 2 (this is the end apple, don't go further)
            if root in visited: 
                return 0
            visited.add(root)
            desc_sum = 0            
            for adj_v in adj_map[root]:
                desc_sum += helper(adj_v)
            if desc_sum > 0:
                return desc_sum + 2
            elif hasApple[root]:
                return 2
            else:
                return 0              
        return max(0, helper(0) - 2)