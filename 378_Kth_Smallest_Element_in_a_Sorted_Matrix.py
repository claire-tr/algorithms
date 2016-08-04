class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        '''
            Algorithm:
            h: list of tuple (element, row, index), which is initialised with first element of each row in the matrix.
            We maintain a heap. In the for loop, we get the smallest element v which is in row r,
            and replace v with the next element in the row r

            Time Complexity:
            insert an element into heap: O(log(n)), where n is the width of the matrix
            find k the k-th element O(k)
            Overall: O(klog(n))
        '''
        from heapq import heappop, heapreplace, heapify
        h = [[matrix[i][0], i, 0] for i in xrange(len(matrix))]
        heapify(h)

        # Since we want to find kth, we pop the first k elements
        for _ in xrange(k-1):
            val, row, col = h[0]
            if col < len(matrix[row]) - 1:
                heapreplace(h,[matrix[row][col+1], row, col + 1])
                # more efficient than push after pop
            else:
                heappop(h)

        return heappop(h)[0]
