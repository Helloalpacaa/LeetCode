class Solution {
    public int rob(int[] nums) {
        int[][] dp = new int[nums.length][2];
        dp[0][0] = 0; // 不抢
        dp[0][1] = nums[0]; // 抢
        for (int i = 1; i < nums.length; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]); // 不抢，前面一个就可以抢
            dp[i][1] = dp[i - 1][0] + nums[i]; // 抢，前面一个就不能抢
        }

        return Math.max(dp[nums.length - 1][0], dp[nums.length - 1][1]);
    }
}