# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return
        near = root.val
        while root:
            if abs(root.val - target) < abs(near - target):
                near = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return near