class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # special_number * 2 + outlier = sum
        # outlier = sum - special_number * 2

        count = Counter(nums)
        max_outlier = float('-inf')
        total = sum(nums)

        for num in count:
            potential_outlier = total - num * 2

            if (potential_outlier in count) and (potential_outlier != num or count[potential_outlier] >= 2):
                max_outlier = max(max_outlier, potential_outlier)
        
        return max_outlier