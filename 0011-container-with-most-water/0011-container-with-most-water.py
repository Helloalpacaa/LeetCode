class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1

        while left < right:
            base = right - left
            area = max(area, base * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return area