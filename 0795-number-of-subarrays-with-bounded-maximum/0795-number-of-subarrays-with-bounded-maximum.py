class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        def countSubarrays(boundry: int) -> int:
            total = 0
            curr = 0
            for num in nums:
                if num <= boundry:
                    curr += 1
                else:
                    curr = 0
                total += curr
            return total
        
        return countSubarrays(right) - countSubarrays(left - 1)