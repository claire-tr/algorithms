# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # DFS Solution

        '''
        if not root:
            return 0
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

         '''

        # BFS Solution
        # Go through row by row, once meet a leaf node, it is the minimum depth

        if not root:
            return 0
        queue = [root]
        level = 1
        while queue:
            # level += 1 after have scanned the whole row
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return level
            level += 1
        return level

