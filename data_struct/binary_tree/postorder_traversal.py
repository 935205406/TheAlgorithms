"""
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        """后续遍历  使用迭代的方式完成

        :param root: 根节点
        :return:
        """
        res = []
        stack = []
        # 每次都入栈两次
        if root is not None:
            stack.append(root)
            stack.append(root)
            while stack:
                node = stack.pop()  # 弹出一个
                # 当弹出的node与更新后的stack中的last node不同时，说明该节点的子节点都处理过了
                # 当相同时，说明没有处理过，要先处理子节点
                if len(stack) > 0 and node == stack[len(stack) - 1]:
                    if node.right is not None:
                        stack.append(node.right)
                        stack.append(node.right)
                    if node.left is not None:
                        stack.append(node.left)
                        stack.append(node.left)
                else:
                    res.append(node.val)
        return res

        # 另一种方式 使用last变量存储上次被处理的node，用于标识 中间节点 是否需要被处理还是压入stack
        # last = TreeNode(0)
        # if root is not None:
        #     stack.append(root)
        #     while stack:
        #         node = stack[len(stack)-1]
        #         if (node.right is None and node.left is None) or (node.right == last or (node.left == last and node.right is None)):
        #             p = stack.pop()
        #             res.append(p.val)
        #             last = p
        #         else:
        #             if node.right is not None:
        #                 stack.append(node.right)
        #             if node.left is not None:
        #                 stack.append(node.left)
        # return res

    def postorder_traversal_recursive(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        left = self.postorder_traversal_recursive(root.left)
        right = self.postorder_traversal_recursive(root.right)
        left.extend(right)
        left.extend([root.val])
        return left


def main():
    node_1 = TreeNode(3)
    node_2 = TreeNode(2)
    node_root = TreeNode(1)
    node_root.right = node_2
    node_2.left = node_1
    solution = Solution()
    # print(solution.postorder_traversal(node_root))
    print(solution.postorder_traversal_recursive(node_root))


if __name__ == '__main__':
    main()
