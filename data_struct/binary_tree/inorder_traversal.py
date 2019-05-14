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

    def inorder_traversal_recursive(self,root: 'TreeNode') -> 'List[int]':
        """中序遍历 使用递归

        :param root: 根节点
        :return:
        """
        left_list = list()
        right_list = list()
        if root is None:
            return []
        if root.left is not None:
            left_list = self.inorder_traversal_recursive(root.left)
        if root.right is not None:
            right_list = self.inorder_traversal_recursive(root.right)
        res = [root.val]
        left_list.extend(res)
        left_list.extend(right_list)
        return left_list


def main():
    node_1 = TreeNode(3)
    node_2 = TreeNode(2)
    root_node = TreeNode(1)
    root_node.right = node_2
    node_2.left = node_1
    solution = Solution()
    # print(solution.inorder_traversal(root_node))
    print(solution.inorder_traversal_recursive(root_node))


if __name__ == '__main__':
    main()
