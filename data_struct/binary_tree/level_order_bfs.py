"""给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）

给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        res = []
        stack = []  # 存储上一层节点
        if root is None:
            return res
        stack.append(root)  # 存储第0层的节点
        res.append([root.val])
        while len(stack) > 0:
            level_nodes_val = []
            cur_level_nodes = []
            while len(stack) > 0:
                node = stack.pop(0)
                if node.left is not None:
                    level_nodes_val.append(node.left.val)
                    cur_level_nodes.append(node.left)
                if node.right is not None:
                    level_nodes_val.append(node.right.val)
                    cur_level_nodes.append(node.right)
            stack.extend(cur_level_nodes)
            if len(level_nodes_val) > 0:
                res.append(level_nodes_val)  # 将这一层节点加入res
        return res


def main():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.right = node_6
    solution = Solution()
    print(solution.level_order(node_1))


if __name__ == '__main__':
    main()
