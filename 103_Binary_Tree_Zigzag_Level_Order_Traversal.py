# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        self.helper(0, results, root)
        return results

    def helper(self, cur, results, root):
        if not root:
            return results
        # Use cur%2 == 0 to replace the zigzag flag
        if cur >= len(results):
            results.append([root.val])
        else:
            if cur%2 == 1:
                results[cur].insert(0, root.val)
            else:
                results[cur].append(root.val)

        self.helper(cur+1, results, root.left)
        self.helper(cur+1, results, root.right)
