# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None


    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # Recursive, deal with the current node after all of its children have been flattened
        # Reverse preorder
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)

        #note this part
        root.right = self.prev
        root.left = None
        self.prev = root