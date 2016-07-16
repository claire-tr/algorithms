class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        '''
            1. Basic Backtracking approach, also deliver a parameter boolean[] to mark
               whether an element has been added to the current result set
            2. To permute n numbers, devide into subproblems:
                we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers,
                in every possible position.
        '''
        res = [[]]

        for n in nums:
            temp_res = []
            for r in res:
                for i in xrange(len(r)+1):
                    temp_res.append(r[:i] + [n] + r[i:])
            res = temp_res
        return res
