# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        '''
        # BFS (recursive)
        return not root or self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        '''

        #DFS (iterative)
        # It's like using stack to simulate the process of recursion
        # But need to pay attention to how to deal with the parts where recursive algorithm's intermediate steps returns True/False
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            elif not l or not r or l.val != r.val:
                return False
            else:
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
        return True
