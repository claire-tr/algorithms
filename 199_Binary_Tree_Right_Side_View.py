# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS
        if not root:
            return []
        queue = [root]
        result = []
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if level == len(result):
                    result.append(node.val)
                # Add right node first, so the first node is the rightmost node, so don't have to store every node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            level += 1
        return result

        # DFS

