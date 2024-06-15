class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            # 这里不能用prefixSum[i] += nums[i - 1], prefixSum[i]本身是0，+= nums[i - 1]只会得到nums[i - 1]
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        
        ans = float('inf')
        queue = deque()
        for j in range(n + 1):
            while queue and prefixSum[j] - prefixSum[queue[0]] >= k:
                ans = min(ans, j - queue.popleft())
            
            while queue and prefixSum[j] < prefixSum[queue[-1]]:
                queue.pop()
            
            queue.append(j)
        
        return -1 if ans == float('inf') else ans
            