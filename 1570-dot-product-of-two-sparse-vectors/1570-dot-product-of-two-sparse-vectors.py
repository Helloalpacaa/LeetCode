class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonZeroValues = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonZeroValues[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotProduct = 0
        for index, value in self.nonZeroValues.items():
            if index in vec.nonZeroValues:
                dotProduct += value * vec.nonZeroValues[index]
        return dotProduct

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)