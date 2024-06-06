class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedSquares = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                sortedSquares[index] = nums[right] ** 2
                right -= 1
            else:
                sortedSquares[index] = nums[left] ** 2
                left += 1
            index -=1
        
        return sortedSquares