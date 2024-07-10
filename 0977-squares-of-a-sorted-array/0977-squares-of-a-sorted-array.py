class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        ans = [0] * len(nums)
        index = len(nums) - 1
        
        while i <= j:
            if nums[i] ** 2 >= nums[j] ** 2:
                ans[index] = nums[i] ** 2
                i += 1
            else:
                ans[index] = nums[j] ** 2
                j -= 1
                
            index -= 1
            
        return ans