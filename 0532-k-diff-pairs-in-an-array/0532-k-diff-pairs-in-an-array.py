class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = Counter(nums)
        count = 0
        
        for i in counter:
            if k == 0 and counter[i] > 1 or k != 0 and i + k in counter:
                count += 1
        
        return count