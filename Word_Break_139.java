import java.util.HashSet;
import java.util.Set;

/**
 * Created by YunyunChen1 on 4/20/16.
 */
public class Word_Break_139 {
    public static boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] breakPoint = new boolean[s.length()];
        System.out.println(breakPoint);
        return false;
    }
    public static void main(String[] args) {
        String s="leetcode";
        // Initialize Set
        Set<String> set = new HashSet() {{
            add("leet");
            add("code");
        }};

        wordBreak(s, set);
    }
}
