# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        from collections import deque, defaultdict
        """
        BFS:
        - put [node, col] into queue at the same time
        - Every left child access col - 1 while right child col + 1
        - This maps node into different col buckets
        - Get col boundary min and max on the fly
        - Retrieve result from cols
        """
        res = []
        if not root:
            return res
        bucket = defaultdict(list)
        queue = deque()
        queue.append([root,0])
        left, right = 0, 0
        while queue:
            node, col = queue.popleft()
            bucket[col].append(node.val)
            if node.left:
                queue.append([node.left, col - 1])
                left = min(left, col - 1)
            if node.right:
                queue.append([node.right, col + 1])
                right = max(right, col + 1)
        for i in range(left, right + 1):
            res.append(bucket[i])
        return res

