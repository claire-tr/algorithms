class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        i, n = 0, lower
        while n <= upper:
            if i >= len(nums):
                if n == upper:
                    res.append(str(upper))
                else:
                    res.append(str(n) + '->' + str(upper))
                return res
            else:
                if nums[i] != n:
                    j = 0
                    while n + j + 1<= upper and nums[i] != n + j + 1:
                        j += 1
                    if j > 0:
                        res.append(str(n) + '->' + str(n+j))
                    else:
                        res.append(str(n))
                    n = n + j + 1
                else:
                    n += 1
                    i += 1

        return res


