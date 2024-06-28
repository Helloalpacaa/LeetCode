class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minStack = deque()
        maxStack = deque()
        i = 0
        ans = 0
        
        for j in range(len(nums)):
            while minStack and nums[j] < minStack[-1]:
                minStack.pop()
            minStack.append(nums[j])
            
            while maxStack and nums[j] > maxStack[-1]:
                maxStack.pop()
            maxStack.append(nums[j])
            
            if maxStack[0] - minStack[0] > limit:
                if nums[i] == maxStack[0]:
                    maxStack.popleft()
                if nums[i] == minStack[0]:
                    minStack.popleft()
                i += 1 # Let's consider the window up to the previous element (j-1), which was still valid
            
            ans = max(ans, j - i + 1)
        
        return ans