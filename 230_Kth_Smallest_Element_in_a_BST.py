# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        '''
            Binary Search (DFS)
        '''
        count = self.countNodes(root.left)
        if k <= count:
            return self.kthSmallest(root.left, k)
        elif k > count + 1:
            return self.kthSmallest(root.right, k - 1 - count)

        return root.val

    def countNodes(self, node):
        if not node:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)