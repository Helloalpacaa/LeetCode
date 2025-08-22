class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo, hi = [], []
        delayed = defaultdict(int)
        lo_size, hi_size = 0, 0

        def prune(heap):
            # Remove elements at heap top that are marked for deletion
            while heap:
                x = -heap[0] if heap is lo else heap[0]
                if delayed[x] > 0:
                    heappop(heap)
                    delayed[x] -= 1
                else:
                    break

        
        def remove(x):
            """ Mark x for deletion and adjust valid size; actual pop when it reaches top."""
            nonlocal lo_size, hi_size
            delayed[x] += 1
            if x <= -lo[0]:
                lo_size -= 1
                if x == -lo[0]:
                    prune(lo)
            else:
                hi_size -= 1
                if hi and x == hi[0]:
                    prune(hi)
            rebalance()

        
        def add(x):
            nonlocal lo_size, hi_size
            if not lo or x <= -lo[0]:
                heappush(lo, -x)
                lo_size += 1
            else:
                heappush(hi, x)
                hi_size += 1
            rebalance()
        
        def rebalance():
            nonlocal lo_size, hi_size
            # Ensure: len(lo) == len(hi) or len(lo) == len(hi) + 1
            if lo_size > hi_size + 1:
                x = -heappop(lo)
                heappush(hi, x)
                lo_size -= 1
                hi_size += 1
                prune(lo)
            elif lo_size < hi_size:
                x = heappop(hi)
                heappush(lo, -x)
                lo_size += 1
                hi_size -= 1
                prune(hi)
        

        def median():
            return float(-lo[0]) if k % 2 else (-lo[0] + hi[0]) / 2.0
        
        # initialize first window
        for i in range(k):
            add(nums[i])
        ans = [median()]

        # add/remove, rebalance, prune tops, and only then read the mediam
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            ans.append(median())
        
        return ans
