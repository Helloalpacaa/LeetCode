class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for j in range(len(nums)):
            while queue and j - queue[0] >= k:
                queue.popleft()
            
            while queue and nums[j] > nums[queue[-1]]:
                queue.pop()
                
            queue.append(j)
            
            if j >= k - 1:
                ans.append(nums[queue[0]])
        
        return ans