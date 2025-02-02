class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        n = len(nums)
        ans = []

        for i in range(n):   
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            if i - queue[0] >= k:
                queue.popleft()
            
            if i >= k - 1:
                ans.append(nums[queue[0]])
        
        return ans

