class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)

        cntNums = Counter(nums)
        cntForb = Counter(forbidden)

        # 1) feasibility
        for v, c in cntNums.items():
            if c + cntForb.get(v, 0) > n:
                return -1

        # 2) count bad positions and max frequency among bad values
        bad = 0
        cntBad = defaultdict(int)
        maxFreq = 0

        for a, f in zip(nums, forbidden):
            if a == f:
                bad += 1
                cntBad[a] += 1
                if cntBad[a] > maxFreq:
                    maxFreq = cntBad[a]

        if bad == 0:
            return 0

        return max((bad + 1) // 2, maxFreq)