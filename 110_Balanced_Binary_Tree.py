# Note that the depth of the two subtrees of every node never differ by more than 1.
# So if one of the node is not balanced, need to return False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return not self.height(root) == -1

    def height(self, node):
        if not node:
            return 0
        l = self.height(node.left)
        r = self.height(node.right)
        if l == -1 or r == -1 or abs(l-r) > 1:
            return -1
        else:
            return 1 + max(l, r)

