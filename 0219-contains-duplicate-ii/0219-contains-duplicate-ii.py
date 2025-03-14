class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurance = {}

        for i, num in enumerate(nums):
            if num in occurance:
                if i - occurance[num] <= k:
                    return True
            occurance[num] = i
        
        return False