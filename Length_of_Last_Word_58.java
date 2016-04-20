/**
 * Created by YunyunChen1 on 4/19/16.
 */
public class Length_of_Last_Word_58 {
    public int lengthOfLastWord(String s) {
        String[] strs = s.split(" ");
        if (strs.length == 0) return 0;
        return strs[strs.length-1].length();

        /*
        return s.trim().length()-s.trim().lastIndexOf(" ")-1;
        */
    }
}
