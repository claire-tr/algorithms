class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # This sorted 2D matrix is equal to a sorted list
        # So just apply Binary Search on the "sorted list"
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n -1
        while l <= r:
            mid = l + (r-l)/2
            if matrix[mid/n][mid%n] < target:
                l = mid + 1
            elif matrix[mid/n][mid%n] > target:
                r = mid - 1
            else:
                return True
        return False
