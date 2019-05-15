"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.depth = 0

    def max_depth(self, root: TreeNode) -> int:
        """先自顶向下的解决问题

        :param root:
        :return:
        """

        self.max_depth_helper(root, 1)
        return self.depth

    def max_depth_helper(self, root: TreeNode, depth: int):
        if root is None:
            self.depth = max(self.depth, depth-1)
            return
        self.max_depth_helper(root.left, depth + 1)
        self.max_depth_helper(root.right, depth + 1)

    def max_depth_bottom_up(self, root: TreeNode):
        """自下向上解决问题

        :param root:
        :return:
        """
        if root is None:
            return 0
        return max(self.max_depth_bottom_up(root.left), self.max_depth_bottom_up(root.right)) + 1


def main():
    node_3 = TreeNode(3)
    node_9 = TreeNode(9)
    node_20 = TreeNode(20)
    node_15 = TreeNode(15)
    node_7 = TreeNode(7)
    node_3.left = node_9
    node_3.right = node_20
    node_20.left = node_15
    node_20.right = node_7
    solution = Solution()
    solution.max_depth(node_3)
    print(solution.depth)
    # print(solution.max_depth_bottom_up(node_3))


if __name__ == '__main__':
    main()
