/**
 * Created by YunyunChen1 on 4/17/16.
 */
public class Implement_strStr_28 {
    /*
     * 1. Similar with common prefix, start with 0, 1, 2, ..., if String.startWith(needle)
     *    But this looks stupid, is there other ways?
     * 2. Brute-force way
     *    public int strStr(String haystack, String needle) {
              for (int i = 0; ; i++) {
                for (int j = 0; ; j++) {
                  if (j == needle.length()) return i;
                  if (i + j == haystack.length()) return -1;
                  if (needle.charAt(j) != haystack.charAt(i + j)) break;
                }
              }
            }
         This approach seems to be the best solution
     */
    public int strStr(String haystack, String needle) {
        for (int i = 0; i <= haystack.length(); i++) {
            for (int j = 0; j <= needle.length(); j++) {
                if (j == needle.length()) return i;
                if (i+j == haystack.length()) return -1;
                if(haystack.charAt(i+j) != needle.charAt(j)) break;
            }
        }
        return -1;
    }
}
