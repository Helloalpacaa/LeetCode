class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9+7
        
        # 1. collect events
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))  # entering
            events.append((x2, y1, y2, -1)) # leaving
        
        # 2. sort events by x
        events.sort()

        # active intervals (list of [y1, y2])
        active = []
        prev_x = events[0][0]
        total_area = 0

        def compute_y_union(intervals):
            if not intervals:
                return 0
            
            intervals.sort()
            total = 0
            curr_start, curr_end = intervals[0]
            for y1, y2 in intervals[1:]:
                if y1 > curr_end:
                    total += curr_end - curr_start
                    curr_start, curr_end = y1, y2
                else:
                    curr_end = max(curr_end, y2)
            
            total += curr_end - curr_start
            return total
        
        for x, y1, y2, typ in events:
            width = x - prev_x
            height = compute_y_union(active)
            total_area += width * height

            if typ == 1:
                active.append([y1, y2])
            else:
                active.remove([y1, y2])

            prev_x = x
        
        return total_area % MOD
