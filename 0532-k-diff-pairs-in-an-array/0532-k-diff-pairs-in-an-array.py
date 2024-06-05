class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numsPair = {}
        
        for num in nums:
            numsPair[num] = numsPair.get(num, 0) + 1
        
        count = 0
        for num in numsPair:
            if k == 0 and numsPair[num] > 1 or k != 0 and num + k in numsPair:
                count += 1
        
        return count