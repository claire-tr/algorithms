
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        '''
        Just walk down from the whole tree's root as long as both p and q are in the same subtree
        (meaning their values are both smaller or both larger than root's).
        This walks straight from the root to the LCA, not looking at the rest of the tree,
        so it's pretty much as fast as it gets.
        '''
        if not root:
            return root
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)