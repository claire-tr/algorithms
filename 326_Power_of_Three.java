class Power_Of_Three {

    /*At first I though this was a question asking whether n % 3 == 0, this should be easy:
      public boolean isPowerOfThree(int n) {
        return n>0 && (n==1 || (n%3==0 && isPowerOfThree(n/3)));
    }
      Or even faster, by:
          public boolean isPowerOfThree(int n) {
            if (n == 0) return false;
            if (n == 1) return true;
            int sum = 0;
            while(n%10 != 0) {
                sum += n%10;
                n /= 10;
            }
            return sum%3 == 0;
        }
      However, for whether n is power of 3, according to discussion, there are other solutions:
      Find the maximum integer that is a power of 3 and check if it is a multiple of the given input. (related post)

        public boolean isPowerOfThree(int n) {
            int maxPowerOfThree = (int)Math.pow(3, (int)(Math.log(0x7fffffff) / Math.log(3)));
            return n>0 && maxPowerOfThree%n==0;
        }
    
        Or simply hard code it since we know maxPowerOfThree = 1162261467:
    
        public boolean isPowerOfThree(int n) {
            return n > 0 && (1162261467 % n == 0);
        }
        There are also other different math methods, I am gonna stop here.
        */
    public boolean isPowerOfThree(int n) {
        int maxPowerOfThree = (int) Math.pow(3, (int) (Math.log(0x7fffffff) / Math.log(3)));
        return n > 0 && maxPowerOfThree % n == 0;
    }
}
  
