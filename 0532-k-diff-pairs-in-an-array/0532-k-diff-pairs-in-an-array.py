class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hm = {}
        
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        count = 0
        for num in hm:
            if k == 0 and hm[num] > 1 or k != 0 and num + k in hm:
                count += 1
        
        return count