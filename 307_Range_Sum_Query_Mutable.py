class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray(object):

    '''
        Two Solution:
            - Binary Indexed Tree:
            - Segment Tree
                    https://discuss.leetcode.com/topic/45266/python-well-commented-solution-using-segment-trees
                    The idea here is to build a segment tree. Each node stores the left and right
                    endpoint of an interval and the sum of that interval. All of the leaves will store
                    elements of the array and each internal node will store sum of leaves under it.
                    Creating the tree takes O(n) time. Query and updates are both O(log n).
    '''

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # helper function to create the segment tree from input array
        def createTree(nums, l, r):
            # corner cases
            if l > r:
                return None
            # leaf nodes
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = l + (r-l)/2
            root = Node(l, r)
            # recursively build the segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)

            # Total stores the sum of all leaves under root
            # aka, those elements lying between(start, end)
            root.total = root.left.total + root.right.total

            return root
        self.root = createTree(nums, 0, len(nums) - 1)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        # Helper function to update a value
        def updateVal(root, i, val):
            # Base case: the actual value will be updated in a leaf
            # The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
            mid = root.start + (root.end - root.start)/2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)

            # Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            return root.total

        return updateVal(self.root, i, val)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        # Helper function to calculate range sum
        # Binary Search to find the node
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            mid = root.start + (root.end - root.start)/2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i > mid:
                return rangeSum(root.right, i, j)
            else:
                # Otherwise, the interval is split, so we calculate the sum recursively
                # By splitting the interval
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)

        return rangeSum(self.root, i, j)
