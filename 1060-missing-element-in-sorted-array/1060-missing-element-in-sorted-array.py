class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        ans = nums[0] + k

        for i in range(1, len(nums)):
            if nums[i] <= ans:
                ans += 1
            else:
                break
        
        return ans