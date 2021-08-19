class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeTraversal:
    def inorder_recursive(self, root: TreeNode):
        if not root:
            return []
        else:
            return self.inorder_recursive(root.left) + [root.val] + self.inorder_recursive(root.right)

    def preorder_recursive(self, root: TreeNode):
        if not root:
            return []
        else:
            return [root.val] + self.preorder_recursive(root.left) + self.preorder_recursive(root.right)

    def postorder_recursive(self, root: TreeNode):
        if not root:
            return []
        else:
            return self.postorder_recursive(root.left) + self.postorder_recursive(root.right) + [root.val]

    def inorder_iterative(root: TreeNode):
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    def preorder_iterative(root: TreeNode):
        res = []
        stack = []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res

    def postorder_iterative(root: TreeNode):
        res = []
        stack = []
        prev = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root.right == None or root.right == prev:
                    stack.pop()
                    res.append(root.val)
                    prev = root
                    root = None *****
                else:
                    root = root.right
        return res

    def inorder_morris(root: TreeNode):
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                rightmost_in_the_left = root.left
                while rightmost_in_the_left.right and rightmost_in_the_left.right != root:
                    rightmost_in_the_left = rightmost_in_the_left.right
                if rightmost_in_the_left.right == None: *****
                    rightmost_in_the_left.right = root
                    root = root.left
                else: # second time in the loop
                    rightmost_in_the_left.right = None
                    res.append(root.val)
                    root = root.right
        return res

    def preorder_morris(root: TreeNode):
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                rightmost_in_the_left = root.left
                while rightmost_in_the_left.right and rightmost_in_the_left.right != root:
                    rightmost_in_the_left = rightmost_in_the_left.right
                if rightmost_in_the_left.right == None:
                    rightmost_in_the_left.right = root
                    res.append(root.val)
                    root = root.left
                else: # second time in the loop
                    rightmost_in_the_left.right = None
                    root = root.right
        return res        

    def postorder_morris(root: TreeNode):
        res = []
        def reverse_in_place(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        dummy_head = TreeNode('D')
        dummy_head.left = root
        node = dummy_head
        while node != None:
            if not node.left:
                node = node.right
            else:
                rightmost_in_the_left = node.left
                while rightmost_in_the_left.right != None and rightmost_in_the_left.right != node:
                    rightmost_in_the_left = rightmost_in_the_left.right
                if rightmost_in_the_left.right == None:
                    rightmost_in_the_left.right = node
                    node = node.left
                else:
                    rightmost_in_the_left = node.left
                    count_in_the_loop = 0
                    while rightmost_in_the_left.right and rightmost_in_the_left.right != node:
                        res.append(rightmost_in_the_left.val)
                        count_in_the_loop += 1
                        rightmost_in_the_left = rightmost_in_the_left.right
                    res.append(rightmost_in_the_left.val)
                    count_in_the_loop += 1
                    reverse_in_place(res, len(res)-1-count_in_the_loop+1, len(res)-1)
                    rightmost_in_the_left.right = None
                    node = node.right
        return res
 
