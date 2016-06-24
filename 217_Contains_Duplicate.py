class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numset = set()
        for n in nums:
            if n in numset:
                return True
            else:
                numset.add(n)
        return False