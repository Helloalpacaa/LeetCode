class SparseVector:
    def __init__(self, nums: List[int]):
        self.hm = {index: value for index, value in enumerate(nums) if value != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotProduct = 0
        for index, value in self.hm.items():
            if index in vec.hm:
                dotProduct += value * vec.hm[index]
        
        return dotProduct

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)