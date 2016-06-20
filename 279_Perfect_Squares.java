public class Solution {
    public int numSquares(int n) {
        int[] cnt = new int[n+1];

        for(int i = 1; i < n+1; i++) {
            int sqrt = (int)Math.sqrt(i);
            int min = Integer.MAX_VALUE;
            for(int j = 1; j <= sqrt; j++)
                min = Math.min(min, cnt[i-j*j]+1);
            cnt[i] = min;
        }
        return cnt[n];
    }
}