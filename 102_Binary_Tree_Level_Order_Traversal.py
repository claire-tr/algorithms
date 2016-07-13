# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        '''
        BFS
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            row = []
            l = len(queue)
            for i in xrange(l):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                row.append(node.val)
            result.append(row)
        return result
        '''

        # Recursion
        result = []
        self.addLevel(0, result, root)
        return result

    def addLevel(self, level, result, root):
        if not root:
            return result
        if level >= len(result):
            result.append([root.val])
        else:
            result[level].append(root.val)
        self.addLevel(level+1, result, root.left)
        self.addLevel(level+1, result, root.right)


