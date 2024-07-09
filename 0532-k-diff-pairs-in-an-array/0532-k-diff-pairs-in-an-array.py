class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        count = 0
        
        for num in counter:
            if k == 0 and counter[num] > 1 or k != 0 and k + num in counter:
                count += 1
        
        return count