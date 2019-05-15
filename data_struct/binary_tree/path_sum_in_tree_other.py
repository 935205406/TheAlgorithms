"""
因为自己提交的代码属于时间最短的。因此找了其他的代码实现
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if (root.left == None) & (root.right == None):
            return root.val == sum
        else:
            return self.hasPathSum(root.left, sum - root.val) | self.hasPathSum(root.right, sum - root.val)
