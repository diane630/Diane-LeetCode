"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        # dfs resursive solution
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        cloned_node = Node(node.val, [])
        self.visited[node] = cloned_node
        for nei_node in node.neighbors:
            cloned_node.neighbors.append(self.cloneGraph(nei_node))
        return cloned_node
        
        # bfs iterative solution
        if not node:
            return node
        visited = {}
        deq = deque([node])
        visited[node] = Node(node.val, [])
        while deq:
            cur_node = deq.popleft()
            for nei in cur_node.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    deq.append(nei)
                visited[cur_node].neighbors.append(visited[nei])
        return visited[node]
            