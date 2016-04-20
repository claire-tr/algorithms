/**
 * Created by YunyunChen1 on 4/20/16.
 */
public class Remove_Duplicate_From_Sorted_Array_II_80 {
    /*
     * Similar like 1, just add a counter for each not-considered-duplicate element
     * But it is stupid, the easy version:
     *
     */

    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i-2])
                nums[i++] = n;
        return i;
    }
}

