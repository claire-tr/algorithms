public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i1 = m-1, i2 = n-1,i = m+n-1;
        while(i2 >= 0 && i1 >= 0) {
            if(nums2[i2] >= nums1[i1]) {
                nums1[i--] = nums2[i2--];
            }else {
                nums1[i--] = nums1[i1--];
            }
        }
        if(i2>=0)
        while(i>=0) {
            nums1[i--] = nums2[i2--];
        }
    }
}
