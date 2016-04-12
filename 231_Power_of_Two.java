/*
1. Similar with power of three, the max power of 2.

2. The power of 2 is always: 10...0, feels like some trick could make use of this fact

3. Using n&(n-1) trick
  https://leetcode.com/discuss/43875/using-n%26-n-1-trick
  bool isPowerOfTwo(int n) {
        if(n<=0) return false;
        return !(n&(n-1));
    }
    
*. Notice that 1 is also power of 2.

*/

    public boolean isPowerOfTwo(int n) {
        return (n>0) && (n & (n-1)) == 0;
    }
