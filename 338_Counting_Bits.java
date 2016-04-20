/*
Divide the integer range into the following groups:
[0],[1],[2,3],[4,5,6,7],[8,9,10,11,12,13,14,15]
The number of bit 1 are:
 0; 1;  1, 2;  1,2,2,3;  1,2,2,3,2,3,3,4.
It's not hard to find the pattern here, =>the previous group itself and add 1 on each element from the previous group

Question is, how to code the pattern?
        Also,?does the odd/even status of the number help you in calculating the number of 1s?

So now I am going to read posts on the discussion board... :)

1. Easy recursive :F[i] = F[i/2] + i%2
    (OMG math problem again!)
    
  public int[] countBits(int num) {
    int[] f = new int[num + 1];
    for (int i=1; i<=num; i++) f[i] = f[i >> 1] + (i & 1); //i>>1
    return f;
  }
  
  CYY: can improve by using dynamic programming (from i = 1 to i = n, store the result into array)
  As I go through the posts, this approach seems to be the (only) best approach, so I am gonna implement it by DP

*/
class Counting_Bits {
  public int[] countBits(int num) {
    int[] f = new int[num + 1];
    for (int i = 1; i <= num; i++)
      f[i] = f[i / 2] + i % 1;
    return f;
  }
}
