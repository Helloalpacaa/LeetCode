class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # n = 1时，只有一种BST
        # n = 2时，①root为1，BST数量 = 左子树的BST数量 * 右子树的BST数量 ②root为2。。。
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]