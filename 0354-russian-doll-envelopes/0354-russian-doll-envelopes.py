class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)

        heights = [env[1] for env in envelopes]
        # dp[i]: 长度为i + 1的LIS的最小end，the smalledst height that ends an increasing subsequence of length i + 1
        dp = []

        for height in heights:
            # 找到height在dp里的位置
            idx = bisect_left(dp, height)
            if idx == len(dp): # 说明height比所有dp里的值都大
                dp.append(height)
            else:
                dp[idx] = height
            # 假设现在dp是[3,4]，遇到2，idx为0，说明2肯定比当前在index为0上的数字小，那么dp变为[2,4]
            # 长度为1的递增数组的最小height为2，这样是为了保留持续递增的可能性
        
        return len(dp)
        