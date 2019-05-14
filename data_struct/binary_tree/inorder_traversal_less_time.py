# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> 'List[int]':
        #     self.res = []
        #     self.helper(root)
        #     return self.res
        # def helper(self,root):
        #     if not root:
        #         return
        #     self.helper(root.left)
        #     self.res.append(root.val)
        #     self.helper(root.right)
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                p = stack.pop()
                res.append(p.val)
                root = p.right
        return res
