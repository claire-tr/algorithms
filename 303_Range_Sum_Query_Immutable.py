class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        self.left = [0] * (n+1)
        self.right = [0] * (n+1)
        for i in range(1, n+1):
            self.left[i] += self.left[i-1] + nums[i-1]
        for i in range(n-2, -1, -1):
            self.right[i] += self.right[i+1] + nums[i+1]
        self.sum = self.left[n]


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum - self.left[i] - self.right[j]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)