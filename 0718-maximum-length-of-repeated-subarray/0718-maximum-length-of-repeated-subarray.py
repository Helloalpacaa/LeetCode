class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)] # m is column, n is row

        for i in range(n):
            for j in range(m):
                if nums1[j] == nums2[i]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        
        return max(max(row) for row in dp)