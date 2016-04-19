/**
 * Created by YunyunChen1 on 4/17/16.
 */
public class Spiral_Matrix_54 {

    /*  Solutions Summary
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
}
