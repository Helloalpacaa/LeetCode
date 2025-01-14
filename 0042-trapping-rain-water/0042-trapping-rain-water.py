class Solution:
    def trap(self, height: List[int]) -> int:
        # 单调递减栈，一旦遇到更大的值，就是接雨水的时候
        monotonic_stack = deque()
        area = 0

        for i in range(len(height)):
            while monotonic_stack and height[i] > height[monotonic_stack[-1]]:
                base = height[monotonic_stack.pop()]
                if monotonic_stack:
                    left = monotonic_stack[-1]
                    area += (i - left - 1) * (min(height[left], height[i]) -  base)
            monotonic_stack.append(i)
        
        return area