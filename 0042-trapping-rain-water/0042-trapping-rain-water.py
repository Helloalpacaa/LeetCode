class Solution:
    def trap(self, height: List[int]) -> int:
        monotonic_stack = []
        ans = 0

        for i in range(len(height)):
            while monotonic_stack and height[i] > height[monotonic_stack[-1]]:
                base = height[monotonic_stack.pop()]
                if monotonic_stack:
                    h = min(height[monotonic_stack[-1]], height[i])
                    ans += (i - monotonic_stack[-1] - 1) * (h - base)
            monotonic_stack.append(i)
        
        return ans
