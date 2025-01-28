class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_common = count.most_common(k)
        ans = [item[0] for item in most_common]

        return ans