public class Solution {
    public boolean wordPattern(String pattern, String str) {
        if(pattern == "" && str == "") return true;
        String[] s = str.split(" ");
        String[] p = pattern.split("");
        if(pattern.length() != s.length)
            return false;
        Map<String, Integer> pt = new HashMap<>();
        Map<String, Integer> st = new HashMap<>();//In the previous test cases, don't have to use two maps, but in the new test cases, the
        for(int i = 0; i < s.length; i++) {       // pattern and the string may be the same string, so use two maps would be better.
            if(!Objects.equals(pt.put(p[i],i),st.put(s[i],i))) 
                return false;
        }
        return true;
    }
}
