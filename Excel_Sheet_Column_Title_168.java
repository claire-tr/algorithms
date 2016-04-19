/**
 * Created by YunyunChen1 on 4/19/16.
 */
public class Excel_Sheet_Column_Title_168 {
    //26进制
    // n-1
    public String convertToTitle(int n) {
        String s = "";
        while (n > 0) {
            n -=1;
            s = (char)('A'+n%26) +s;
            n /= 26;
        }
        return s;
    }
}
