class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        left, up, right, down = 0, 0, len(matrix[0])-1, len(matrix)-1
        while left <= right and up <= down:
            # Go right
            for j in range(left, right+1):
                res.append(matrix[up][j])
            up += 1
            # Go down
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            # Go left
            if right >= left and up <= down:
                for j in range(right, left-1, -1):
                    res.append(matrix[down][j])
            down -= 1
            # Go up
            if up <= down and left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
            left += 1
        return res

    '''
   /*  Solutions Summary
        cyy on 4/17/16.
     * 1. Use four variables: rowBegin, rowEnd, colBegin, colEnd
     *    while (rowBegin <= rowEnd && colBegin <= colEnd)
     *    Traverse from rowBegin -> rowEnd, after iteration, rowBegin++
     *    Traverse from colBegin -> colEnd, after iteration, colEnd--
     *    (Tricky part), if (rowBegin <= rowEnd) colEnd -> colBegin, after iteration, rowEnd--
     *    Note the if judgement, colEnd>=colBegin is already judged in the for loop, but the rowEnd >= rowBegin needs judgement.
     *
     *    Note: Corner cases, termination condition in multiple while/for loop
     *
     *
     *    2. (Game Developer) Use direction offset
     *       Don't need to check the border
     *       int dirs[4][2] = {{1,0},{0,-1},{-1,0},{0,1}};
     *       pos[0] += dir[d][0]; pos[1] += dirs[d][1];
     *       result.push_back(matrix[pos[0]][pos[1]]);
     *       Use d = (d+1)%4 to loop between direction offsets
     *       swap m, n index to switch between horizontal and vertical mode
     */
    '''
