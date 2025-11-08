class Solution:
    def trap(self, height: List[int]) -> int:
        # monotonic stack
        # only store elements that smaller than the top of the stack, and pop it when see a larger value
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < height[i]:
                base = height[stack.pop()]
                if stack:
                    left = stack[-1]
                    area = (i - left - 1) * (min(height[left], height[i]) - base)
                    res += area
            stack.append(i)
        
        return res
            