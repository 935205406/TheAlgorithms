"""
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        """迭代方式实现中序遍历

        参考了前序遍历中，网站所给出的最短用时代码的思想

        :param root: 根节点对象
        :return:
        """
        res = list()
        stack = list()
        if root is None:
            return res
        while True:
            if root is not None:
                if root.left is not None:  # 左子节点存在
                    next_root = root.left
                    root.left = None
                    stack.append(root)  # 先暂存中间节点
                    root = next_root
                elif root.left is None:  # 如果左子节点不存在，则可以直接添加该节点的值
                    res.append(root.val)
                    if root.right is not None:
                        root = root.right
                    elif len(stack) > 0:
                        root = stack.pop()
                    else:
                        break
        return res
