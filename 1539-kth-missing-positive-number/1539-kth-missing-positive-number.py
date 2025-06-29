class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = 1
        count = 0
        i = 0
        while count < k:
            if i < len(arr) and arr[i] == n:
                i += 1
            else:
                count += 1
            n += 1
        
        return n - 1