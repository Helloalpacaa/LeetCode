class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        
        queue = deque()
        ans = float('inf')
        for i in range(n + 1):
            while queue and prefixSum[i] - prefixSum[queue[0]] >= k:
                ans = min(ans, i - queue[0])
                queue.popleft()
            
            while queue and prefixSum[i] < prefixSum[queue[-1]]:
                queue.pop()
            
            queue.append(i)
        
        return -1 if ans == float('inf') else ans
        
        
        
        