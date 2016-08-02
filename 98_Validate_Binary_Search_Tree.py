# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidSubtree(root, -sys.maxint, sys.maxint)

    def isValidSubtree(self, root, local_min, local_max):
        if not root:
            return True
        if root.val <= local_min or root.val >= local_max:
            return False
        return self.isValidSubtree(root.left, local_min, root.val) and self.isValidSubtree(root.right, root.val, local_max)

    