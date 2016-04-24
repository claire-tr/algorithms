/**
 * Created by YunyunChen1 on 4/20/16.
 */
public class Ugly_Number_263 {
    /*
     * Definition of ugly number: positive numbers whose prime factors only include 2, 3, 5.
     * Solution: Divide up the number with each factor, see whether the result equals to 1.
     * (Not certain of it yet) keep concise
     * (Maybe we should be concise, but we shouldn't care about the concise too much that lose readability)
     */
    public boolean isUgly(int num) {
        for (int i = 2; i < 6 && num > 0; i++) {
            while(num % i == 0)
                num /= i;
        }

        return num == 1;
    }
}
