# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        if not root:
            return results
        self.pathHelper(root, [], results, sum)
        return results

    def pathHelper(self, root, path, results, sum):
        path.append(root.val)
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                results.append([p for p in path])
                return
            else:
                return
        else:
            if root.left:
                self.pathHelper(root.left, path, results, sum)
                path.pop()
            if root.right:
                self.pathHelper(root.right, path, results, sum)
                path.pop()

        