/*
Two approaches:

1. Use XOR:

public int missingNumber(int[] nums) {

    int xor = 0, i = 0;
    for (i = 0; i < nums.length; i++) {
        xor = xor ^ i ^ nums[i];
    }

    return xor ^ i;
}

2. Use the sum

public static int missingNumber(int[] nums) {
    int sum = nums.length;
    for (int i = 0; i < nums.length; i++)
        sum += i - nums[i];
    return sum;
}

*/
