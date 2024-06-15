class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = collections.deque() # anscending monotonic stack with the min value at the first index
        maxQ = collections.deque() # descending monotonic stack with the max value at the first index
        i = 0
        ans = 0
        
        for j in range(len(nums)):
            # maintain a ascending monotonic stack
            while minQ and nums[j] < minQ[-1]:
                minQ.pop()
            # maintain a descending monotonic stack
            while maxQ and nums[j] > maxQ[-1]:
                maxQ.pop()
            
            minQ.append(nums[j])
            maxQ.append(nums[j])
            
            # move i to a new start of valid window until pops the element causing the diff
            while maxQ[0] - minQ[0] > limit:
                if minQ[0] == nums[i]:
                    minQ.popleft()
                if maxQ[0] == nums[i]:
                    maxQ.popleft()
                i += 1
            
            ans = max(ans, j - i + 1)
            
        return ans
        