class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        sortedSquares = []
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                sortedSquares.append(nums[j] ** 2)
                j -= 1
            else :
                sortedSquares.append(nums[i] ** 2)
                i += 1
                
        return sortedSquares[::-1]