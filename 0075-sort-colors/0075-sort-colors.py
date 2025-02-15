class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Count occurrences of each color
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        # Fill the array with the right number of each color
        index = 0
        for i in range(3):
            while count[i] > 0:
                nums[index] = i
                index += 1
                count[i] -= 1