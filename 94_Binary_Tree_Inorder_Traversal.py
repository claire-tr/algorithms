# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        stack = []
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            else:
                break

        return res