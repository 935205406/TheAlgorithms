"""
提交的解答，运行时间最短，且和其他人的解答类似。
因此该文件用于记录找到的别人使用迭代方式来求解的代码
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]

        while (queue):
            # 下一层所有节点
            next_queue = list()
            # 当前层节点的值
            layer = list()
            # 得到下一层节点、当前节点的值
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)

            if layer != layer[::-1]:
                return False
            queue = next_queue

        return True