class Solution {
    public int maxProfit(int[] prices) {
        // Greedy
        /*
        int count = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                count += (prices[i] - prices[i - 1]);
            }
        }
        return count;
        */

        // dp
        int[][] dp = new int[prices.length][2];
        // dp[i][0] = 持股，dp[i][1] = 不持股
        dp[0][0] = -prices[0];
        dp[0][1] = 0;
        for (int i = 1; i < prices.length; i++) {
            // 持股: 之前就持股 or 之前不持股, 今日买入
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
            // 不持股：之前就不持股 or 之前持股, 今日卖出
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] + prices[i]);
        }
        return dp[prices.length - 1][1];
    }
}