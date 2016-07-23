class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convert(self, str):
        root = cur = TreeNode(str[0])
        stack = [root]
        for i in xrange(1, len(str), 2):
            if str[i] == '?':
                # left child
                node = stack[-1]
                node.left = TreeNode(str[i+1])
                stack.append(node.left)
            elif str[i] == ':':
                stack.pop()
                node = stack.pop()
                node.right = TreeNode(str[i+1])
                stack.append(node.right)
        return root
