/**
 * Created by YunyunChen1 on 4/16/16.
 */
public class Remove_Element_27 {

        public int removeElement(int[] nums, int val) {
            int len = 0;
            for(int i = 0; i < nums.length; i++) {
                if(nums[i] != val)
                    nums[len++] = nums[i];
            }
            return len;
        }
// Can also swap with the last element, but need to judge whether after swap, the current value is still val.
}
