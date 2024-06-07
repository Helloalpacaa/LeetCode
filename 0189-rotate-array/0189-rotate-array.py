class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swipe(nums: List[int], i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        k = k % len(nums)
        swipe(nums, 0, len(nums) - 1)
        swipe(nums, 0, k - 1)
        swipe(nums, k, len(nums) - 1)