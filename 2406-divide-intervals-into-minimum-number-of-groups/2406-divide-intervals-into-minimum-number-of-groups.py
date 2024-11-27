class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # 1, 1, 2, 5, 6
        # 3, 5, 8, 10, 10
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        
        start.sort()
        end.sort()

        j = 0
        groups = 0
        for i in range(len(start)):
            if start[i] <= end[j]:
                groups += 1
            else:
                j += 1
        
        return groups
