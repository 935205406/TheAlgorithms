class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        """自下向上

        :param root:
        :return:
        """
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

    def max_depth_bottom_up(self,root: TreeNode):
        """自上而下

        :param root:
        :return:
        """
        if not root:
            return 0
        q = []
        q.append(root)
        depth = 0
        while len(q) != 0:
            depth += 1
            for i in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]
        return depth
