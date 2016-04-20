class House_Robber {
    public int rob(int[] nums) {
        /*
        int[][] dp = new int[nums.length+1][2];
        for(int i = 1; i < nums.length+1; i++) {
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = dp[i-1][0] + nums[i-1];
        }
        return Math.max(dp[nums.length][0], dp[nums.length][1]);
        */
        if(nums.length == 0) return 0;
        int preNo = 0, preYes = nums[0];
        for(int i = 1; i < nums.length; i++) {
            int tmp = preNo;
            preNo = Math.max(preNo, preYes);
            preYes = tmp + nums[i];
        }
        return Math.max(preNo, preYes);
    }
}