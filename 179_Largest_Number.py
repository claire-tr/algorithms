class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        # https://leetcode.com/discuss/21550/my-3-lines-code-in-java-and-python
        # Define a comparator based on x+y and x+y
        # if x+y > y+x (concatenate strings), then x > y
        nums = [str(n) for n in nums]
        nums.sort(cmp=lambda x, y:cmp(y+x, x+y))
        res = ''.join(nums).lstrip('0') or '0'
        # lstring(): Return a copy of the string with leading characters removed
        return res
