class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        It's recursive and expands the meaning of the function.
        If the current (sub)tree contains both p and q, then the function result is their LCA.
        If only one of them is in that subtree, then the result is that one of them.
        If neither are in that subtree, the result is null/None/nil.
        """
        if not root:
            return None
        if root == p or root == q:
            return root

        l, r = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        else:
            return l if l else r