class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        for i in range(len(intervals)):
            if i > 0 and intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans