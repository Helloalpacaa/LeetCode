class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        // dp[j]: 截止到s[j-1]有多少种decode的方法，因为这题必须用到dp[i-2]，所以把j往后移一位
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) == '0' ? 0 : 1;
        for (int i = 2; i <= n; i++) {
            int first = Integer.parseInt(s.substring(i - 1, i));
            int second = Integer.parseInt(s.substring(i - 2, i));
            if (first > 0) { // 当前character不为0，那么它可以单独decode
                dp[i] += dp[i - 1]; // 其实就是dp[i] = dp[i - 1]，
            }
            if (second >= 10 && second <= 26) { // 保证了这个两位数的第一位不为0,如果valid这个二位数就可以单独decode
                dp[i] += dp[i - 2];
            }
        }
        return dp[n];
    }

}