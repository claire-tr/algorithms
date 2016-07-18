class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Iterative

        class Solution(object):
            def permuteUnique(self, nums):
                """
                :type nums: List[int]
                :rtype: List[List[int]]
                """
                '''
                Don't need to sort
                To handle duplication, just avoid inserting a number before any of its duplicates.
                '''
                results = [[]]
                for n in nums:
                    temp_res = []
                    for r in results:
                        for i in xrange(len(r) + 1):
                            temp_res.append(r[:i] + [n] + r[i:])
                            if i < len(r) and r[i] == n:
                                break
                    results = temp_res
                return results




        '''
        # Recursive
        # Use an extra boolean array boolean[] used to indicate
          whether an element has been added to the current result
        # Sort the array to make sure we can skip the same value
        # When a number has the same value with previous, we only
          use the number if its previous has been used before

        results = []
        nums.sort()
        self.helper(nums, [], results, [False]* len(nums))
        return results

    def helper(self, nums, res, results, used):
        if len(res) == len(nums):
            results.append(list(res))
            return
        for i in xrange(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                continue
            res.append(nums[i])
            used[i] = True
            self.helper(nums, res, results, used)
            res.pop()
            used[i] = False
        '''
