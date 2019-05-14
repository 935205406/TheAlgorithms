# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """ 使用迭代的方式
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        stack = list()
        if root is None:
            return result
        while True:
            if root is not None:
                result.append(root.val)
                if root.left is not None:
                    if root.right is not None:
                        stack.append(root.right)
                    root = root.left
                elif root.right is not None:
                    root = root.right
                elif len(stack) > 0:
                    root = stack.pop()
                else:
                    break
        return result

    def pre_order(self, root, result):
        ''' 使用递归的方式
        先序
        :param root:
        :return:
        '''
        if root is None:
            return
        result.append(root.val)
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)