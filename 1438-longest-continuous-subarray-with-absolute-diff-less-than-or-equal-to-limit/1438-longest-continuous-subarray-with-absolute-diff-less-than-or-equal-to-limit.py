class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxStack = deque()
        minStack = deque()
        ans = 0
        i = 0
        
        for j in range(len(nums)):
            while maxStack and nums[j] > nums[maxStack[-1]]:
                maxStack.pop()
            maxStack.append(j)
            
            while minStack and nums[j] < nums[minStack[-1]]:
                minStack.pop()
            minStack.append(j)
            
            while minStack and maxStack and nums[maxStack[0]] - nums[minStack[0]] > limit:
                if i == minStack[0]:
                    minStack.popleft()
                if i == maxStack[0]:
                    maxStack.popleft()
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans
            
            