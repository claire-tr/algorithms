/**
 * Created by YunyunChen1 on 4/17/16.
 */
public class Longest_Common_Prefix_14 {
    /*
     * Brute-force way is easy, increment the prefix from str[0][0] -> str[0][str[0].length-1], compare each string in the array
     * (Incremental)
     *
     * A more efficient way:
     * (Decremental)
     *      start from str[0].substring(0, str[0].length())
     *      Go through the array, cutting the prefix to fit each string
     *      if the string doesn't fit the prefix, pre = pre.substring(0, pre.length()-1);
     */

    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length == 0) return "";
        String pre = strs[0];
        for(int i = 1; i < strs.length; i++) {
            while(!strs[i].startsWith(pre))
                pre = pre.substring(0, pre.length()-1);
        }
        return pre;
    }
}
