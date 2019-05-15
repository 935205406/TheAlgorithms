"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """时间处于最短的部分，因此该实现不再生成 *_less_time.py 文件，而是产生一个使用迭代器解题的 *_iterator.py 文件

        :param root:
        :return:
        """
        if root is None:
            return True
        return self.recursive_tree(root.left, root.right)

    def recursive_tree(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.recursive_tree(left.left, right.right) and self.recursive_tree(left.right, right.left)
        return False
