/**
 * Created by YunyunChen1 on 4/19/16.
 */
public class Remove_Duplicate_From_Sorted_Array_26 {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int pre = nums[0], m = 1, n = 1;
        while(n < nums.length) {
            if(nums[n] != pre) {
                nums[m++] = nums[n];
                pre = nums[n];
            }
            n++;
        }
        return m;
    }
}
