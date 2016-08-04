class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
            1. Brute Force O((m+n)log(m+n))
               Merge Sort the two array and find the median
            2. O(n)
               No need to finish the merge sort. Use two pointers, until find the (m+n)th element
            3. Binary Search:

               To solve this problem, we need to understand "What is the use of median".
               In statistics, the median is used for dividing a set into two equal length subsets,
               that one subset is always greater than the other.

               1) len(left_part) == len(right_part)
               2) max(left_part) <= min(right_part)

               Divide 2 arrays into 4 sections in half, at each round throw out 1 section.

               Runtime:O(log4(m+n)) = O(log(m + n))


        '''
        def kth(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]

            m, n = len(nums1)/2, len(nums2)/2

            if k > (m + n):
                if nums1[m] < nums2[n]:
                    return kth(nums1[m+1:], nums2, k - m - 1)
                else:
                    return kth(nums1, nums2[n+1:], k - n - 1)
            else:
                if nums1[m] < nums2[n]:
                    return kth(nums1, nums2[:n], k)
                else:
                    return kth(nums1[:m], nums2, k)

        l = len(nums1) + len(nums2)
        if l & 1:
            return kth(nums1, nums2, l/2)
        else:
            return (kth(nums1, nums2, l/2 - 1) + kth(nums1, nums2, l/2))/2.0
