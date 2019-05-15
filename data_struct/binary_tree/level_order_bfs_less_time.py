class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'list[list[int]]':
        if root is None:
            return []

        queue = list()
        queue.append((root, 0))
        map = dict()
        while len(queue) > 0:
            node, level = queue.pop(0)  # type:TreeNode,int
            if node is None:
                continue
            if level not in map.keys():
                map[level] = [node.val]
            else:
                map[level].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        keys = list(map.keys())
        keys.sort()
        result = list()
        for key in keys:
            result.append(map[key])
        return result


    def levelOrder2(self, root: TreeNode) -> 'List[List[int]]':
        """这是看到的另一个解法

        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        cur_node = [root]
        next_node = []
        res.append([i.val for i in cur_node])
        while cur_node or next_node:
            for node in cur_node:
                if node.left:
                    next_node.append(node.left)

                if node.right:
                    next_node.append(node.right)

            if next_node:
                res.append([i.val for i in next_node])

            cur_node = next_node
            next_node = []

        return res
