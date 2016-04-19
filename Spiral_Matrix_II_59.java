/**
 * Created by YunyunChen1 on 4/17/16.
 */
public class Spiral_Matrix_II_59 {
    /*
     * Similar with Spiral Matrix, construct a empty n*n array, traverse the array, fill each element in.

     */
    public int[][] generateMatrix(int n) {
        int[][] nums = new int[n][n];
        int rowBegin = 0, rowEnd = n-1, colBegin = 0, colEnd = n-1;
        int number = 1;
        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            //Go right
            for(int i = colBegin; i <= colEnd; i++) {
                nums[rowBegin][i] = number++;
            }
            rowBegin++;
            //Go down
            for(int i = rowBegin; i <= rowEnd; i++)
                nums[i][colEnd] = number++;
            colEnd--;
            //Go left
            if(rowEnd >= rowBegin)
                for(int i = colEnd; i >= colBegin; i--)
                    nums[rowEnd][i] = number++;
            rowEnd--;
            //Go up
            if(colEnd >= colBegin)
                for(int i = rowEnd; i >= rowBegin; i--)
                    nums[i][colBegin] = number++;
            colBegin++;
        }
        return nums;
    }
}
