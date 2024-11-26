class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0] * len(w)
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i]
        

    def pickIndex(self) -> int:
        rand = random.randint(1, self.prefix_sum[-1])
        return bisect_left(self.prefix_sum, rand)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()