class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        ans = float('inf')
        queue = deque()
        
        for i in range(len(nums) + 1):
            while queue and prefixSum[i] - prefixSum[queue[0]] >= k:
                ans = min(ans, i - queue[0])
                queue.popleft()
            
            while queue and prefixSum[i] < prefixSum[queue[-1]]:
                queue.pop()
            
            queue.append(i)
        
        return ans if ans != float('inf') else -1
                
            
                
                