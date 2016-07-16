# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        '''
            Recursive: O(nlogn)
            preorder: root, left subtree, right subtree
            inorder: left subtree, root, right subtree
            we can know that preorder[0] is always the root of the current subtree, by looking up root
            in inorder, we can split the inorder array into :left subtree, root, right subtree.
            Recursively repeating this process, we can build the tree.
        '''

        '''
            Iterative:
            https://discuss.leetcode.com/topic/795/the-iterative-solution-is-easier-than-you-think
            1. Keep pushing the nodes from the preorder into a stack
            (and keep making the tree by adding nodes to the left of the previous node)
            until the top of the stack matches the inorder.

            2. At this point, pop the top of the stack until the top does not equal inorder
            (keep a flag to note that you have made a pop).

            3. Repeat 1 and 2 until preorder is empty. The key point is that whenever the flag is set,
            insert a node to the right and reset the flag.

        '''
        # Corner case and leaf node
        if len(inorder) == 0:
            return None
        mid = inorder.index(preorder.pop(0)) # Have to pop the root
        root = TreeNode(inorder[mid])
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid+1:])
        return root
