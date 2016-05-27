import java.util.HashSet;
import java.util.Set;

/**
 * Created by YunyunChen1 on 4/20/16.
 */
public class Word_Break_139 {
    public static boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] breakPoint = new boolean[s.length()+1];
        breakPoint[0] = true;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length()+1; j++) {
                if(breakPoint[i] && wordDict.contains(s.substring(i, j)))
                breakPoint[j] = true;
                // why we can break here??
            }
        }
        return breakPoint[s.length()];
    }
    public static void main(String[] args) {
        String s="leetcode";
        // Initialize Set
        Set<String> set = new HashSet() {{
            add("leet");
            add("code");
        }};

        System.out.println(wordBreak(s, set));
    }
}
