/**
 * Created by YunyunChen1 on 4/17/16.
 */
public class Valid_Palindrome_125 {
    /*
     * Two pointers, meet at midpoint
     * Need to judge whether the current character is letter or digit, also ignore the cases
     *
     * Note that Character operation is usually faster than Regex, bc Regex one will create a new string if you call
     * replaceAll(), which is slow and used O(N) space
     */
    public boolean isPalindrome(String s) {
        if (s == "") return true;
        int head = 0, tail = s.length() - 1;
        while(head <= tail) {
            while(!Character.isLetterOrDigit(s.charAt(head)) && head<tail)
                head++;
            while(!Character.isLetterOrDigit(s.charAt(tail)) && head<tail)
                tail--;
            if(Character.toLowerCase(s.charAt(head)) != Character.toLowerCase(s.charAt(tail))) {
                return false;
            }
            head++;
            tail--;
        }

        return true;
    }

}
