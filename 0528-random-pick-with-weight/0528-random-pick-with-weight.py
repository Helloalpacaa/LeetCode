class Solution:

    def __init__(self, w: List[int]):
        # [1, 3]
        # [1, 4]
        # pick a random number from [1, 4], chances of it locates to [1] is 1/4, chances it locates to [2, 3, 4] is 3/4
        self.prefix_sum = [0] * len(w)
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i]

    def pickIndex(self) -> int:
        # pick a random number from [1, self.prefix_sum[-1]]
        rand = random.randint(1, self.prefix_sum[-1])
        # use binary search to find where the random number should be located
        index = bisect_left(self.prefix_sum, rand)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()