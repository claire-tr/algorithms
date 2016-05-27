/**
 * Created by YunyunChen1 on 4/20/16.
 */
public class Pow_50 {
    /*
     * It's easy to implement the brute-force way, with a runtime as O(n)
     * It can be reduced to O(logn) by using recursion
     * Need to pay attention whether n is positive or negative
     */
    public static double myPow(double x, int n) {
        if(n == 0) return 1;
        if(n < 0) {
            x = 1.0/x;
            n *= -1;
        }
        if(n%2 == 0)
            return myPow(x*x, n/2);
        else
            return x*myPow(x*x, n/2);
    }
    public static void main(String[] args) {
        System.out.println(myPow(2,-2));
    }
}
