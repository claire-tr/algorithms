# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.helper(root, [], res)
        return res

    def helper(self, node, path, res):
        path.append("%s->"%node.val)
        if not node.left and not node.right:
            res.append(''.join(path)[:-2])
            return
        if node.left:
            self.helper(node.left, path, res)
            path.pop()
        if node.right:
            self.helper(node.right, path, res)
            path.pop()
