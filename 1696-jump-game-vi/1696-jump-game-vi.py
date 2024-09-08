class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        # dp[i]: 到达index i所能获得的最大score
        dp[0] = nums[0]
        # 一个最大长度为k的单调递减的sliding window
        window = deque([0])

        for i in range(1, n):
            if window[0] < i - k:
                window.popleft()
            
            dp[i] = nums[i] + dp[window[0]]

            while window and dp[window[-1]] < dp[i]:
                window.pop()
            
            window.append(i)
        
        return dp[n - 1]
