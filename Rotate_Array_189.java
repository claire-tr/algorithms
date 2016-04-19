/**
 * Created by YunyunChen1 on 4/18/16.
 */
public class Rotate_Array_189 {
    /*
     * First, reverse the first n-k elements
     * Then, reverse the last k elements
     * Then, reverse all the n elements
     */
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        reverse(nums, 0, nums.length-k-1);
        reverse(nums, nums.length-k , nums.length-1);
        reverse(nums, 0, nums.length-1);
    }

    private void reverse(int[] nums, int start, int end) {
        if (start < 0 || end > nums.length - 1) return;
        while (start < end) {
            int tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;
        }
    }
}
