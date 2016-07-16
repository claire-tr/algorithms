class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        '''
            1. Find the largest index (Scan from right to left), such that nums[k] < nums[k+1], if no such
               index exists, means that the permutation is sorted in descending order, just need to reverse
               it to ascending order (if k == -1, reverse the whole array).
            2. Find the largest index l greater than k such that nums[k] < nums[l]
               (Scan from right to left, find the first index that nums[l] > nums[k])
            3. Swap the value of nums[k] with that of nums[l]
            4. Reverse the sequence from nums[k+1] up to and including the final element nums[len(nums)-1]
        '''
        i = len(nums) - 1
        j = -1
        while i > 0:
            if nums[i-1] < nums[i]:
                j = i-1
                break
            i -= 1
        for i in xrange(len(nums)-1, -1, -1):

            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                # print nums
                #reverse
                nums[j+1:] = sorted(nums[j+1:])
                # for k in xrange(1, (len(nums) - j)/2):
                #     print (len(nums) - j)/2
                #     # print 'reverse'
                #     nums[j+k], nums[len(nums)-k] = nums[len(nums)-k], nums[j+k]
                # print nums
                return
