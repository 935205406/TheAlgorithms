"""
前序遍历使用递归实现
如：
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        """前序遍历 递归实现

        前序遍历：根节点 -> 左子节点 -> 右子节点

        :param root: 根节点对象
        :return:
        """
        if root is None:
            return []
        left_list = []
        right_list = []
        if root.left is not None:
            left_list = self.preorder_traversal(root.left)
        if root.right is not None:
            right_list = self.preorder_traversal(root.right)
        res = [root.val]
        res.extend(left_list)
        res.extend(right_list)
        return res


def main():
    node_1 = TreeNode(3)
    node_2 = TreeNode(2)
    node_2.left = node_1
    root_node = TreeNode(1)
    root_node.right = node_2
    solution = Solution()
    print(solution.preorder_traversal(root_node))


if __name__ == '__main__':
    main()
