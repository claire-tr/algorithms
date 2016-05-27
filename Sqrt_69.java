/**
 * Created by YunyunChen1 on 4/20/16.
 */
public class Sqrt_69 {
    /*
     * Similar to Pow, use binary search to reduce the runtime from O(n) to O(logn)
     * Pay attention to the boudary in BST!!!
     * Think more ahead!
     */

    public static int mySqrt(int x) {
        if (x == 0) return 0;
        int l = 1, r = x;
        while(true) {
            int m = l + (r - l) / 2;
            if (m > x / m)
                r = m - 1;
            else {
                if ((m + 1) > x / (m + 1))
                    return m;
                else
                    l = m + 1;
            }
        }
    }
    public static void main(String[] args) {
        System.out.println(mySqrt(127));
    }
}
