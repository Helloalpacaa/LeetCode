class Solution:

    def __init__(self, w: List[int]):
        # [1, 3, 8, 9]
        # [1, 4, 12, 21]
        self.prefix_sum = [0] * len(w)
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i]
    
    def binarySearch(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def pickIndex(self) -> int:
        rand = random.randint(1, self.prefix_sum[-1])
        index = self.binarySearch(self.prefix_sum, rand)
        return index
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()