class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # Similar to number of islands, replace "x" with 0 to avoid confusion
        # Need to mention that we replacing, when meet 0, need to keep it zero,
        # because we may need to change based on that zero afterwards

        m = len(matrix)
        n = len(matrix[0])

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    for k in xrange(0, m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "x"
                    for k in xrange(0, n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "x"

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == "x":
                    matrix[i][j] = 0
