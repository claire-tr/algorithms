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
        if not root:
            return True
        return self.isValidSubtree(root, -sys.maxint, sys.maxint)

    def isValidSubtree(self, root, local_min, local_max):
        if root.left:
            if not (local_min < root.left.val < root.val and self.isValidSubtree(root.left, local_min, root.val)):
                return False
        if root.right:
            if not (local_max > root.right.val > root.val and self.isValidSubtree(root.right, root.val, local_max)):
                return False
        return True
