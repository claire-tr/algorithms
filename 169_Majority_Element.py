class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        1. Hash Table
        2. Sort, get the nums[n/2]
        3. Randomization: Random pick an element(rand()%n), see if it the is majority one.
           If not, random pick again until find the one.
        4. Divide and Conquer
            https://leetcode.com/discuss/42929/6-suggested-solutions-in-c-with-explanations
        5. Moore Voting Algorithm
            https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
            The majority vote problem is to determine in any given sequence of choices whether there is
            a choice with more occurrences than half of the total number of choices in the sequence and
            if so, to determine this choice.
            Note how this definition contrasts with the mode in which it is
            not simply the choice with the most occurrences,
            but the number of occurrences relative to the total length of the sequence.
        '''
        maj = nums[0]
        cnt = 1
        for i in xrange(1, len(nums)):
            if nums[i] == maj:
                cnt += 1
            else:
                if cnt == 0:
                    maj = nums[i]
                else:
                    cnt -= 1
        return maj