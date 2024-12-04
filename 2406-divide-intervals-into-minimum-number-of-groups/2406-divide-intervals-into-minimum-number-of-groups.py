class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # [1, 1, 2, 5, 6]
        # [3, 5, 8, 10, 10]

        # find each interval's start and end time, then sort them
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        
        start.sort()
        end.sort()

        # use two pointers to track the current start time and end time
        # if start time < end time, there is overlapping and we need to increment the group numbers
        j = 0
        groups = 0
        for i in range(len(start)):
            if start[i] <= end[j]:
                groups += 1
            else:
                j += 1
        
        return groups