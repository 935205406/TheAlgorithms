class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        self.result = list()
        self.poster(root)
        return self.result

    def poster(self,root:'TreeNode'):
        if root != None:
            self.poster(root.left)
            self.poster(root.right)
            self.result.append(root.val)