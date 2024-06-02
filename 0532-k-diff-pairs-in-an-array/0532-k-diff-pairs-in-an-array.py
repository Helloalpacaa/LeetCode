class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = {}
        for num in nums:
            pairs[num] = pairs.get(num, 0) + 1
        
        count = 0
        for key in pairs.keys():
            if (k == 0 and pairs[key] > 1) or (k != 0 and key + k in pairs):
                count += 1
        
        return count