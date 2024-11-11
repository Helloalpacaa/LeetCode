class Solution:
    def trap(self, height: List[int]) -> int:
        # Descending monotonic stack, storing the index of height
        stack = deque()
        n = len(height)
        area = 0

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                base = height[stack.pop()]
                if stack:
                    left = stack[-1]
                    width = i - left - 1
                    area += width * (min(height[left], height[i]) - base)
            stack.append(i)
        
        return area
            

