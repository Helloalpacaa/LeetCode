class Solution:
    def trap(self, height: List[int]) -> int:
        # stack = []
        # water = 0

        # for i in range(len(height)):
        #     while stack and height[i] > height[stack[-1]]:
        #         base = height[stack.pop()]
        #         if stack:
        #             left = stack[-1]
        #             area = (i - left - 1) * (min(height[left], height[i]) - base)
        #             water += area
                
        #     stack.append(i)

        # return water

        # the highest wall can be seen from left and right
        left_max, right_max = 0, len(height) - 1
        water = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left_max] < height[right_max]:
                left += 1
                if height[left] < height[left_max]:
                    water += height[left_max] - height[left]
                else:
                    left_max = left
            else:
                right -= 1
                if height[right] < height[right_max]:
                    water += height[right_max] - height[right]
                else:
                    right_max = right
        
        return water
