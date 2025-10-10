class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y == target or x == target or y == target:
            return True
        
        start = (0, 0)
        seen = {start}
        queue = deque([start])

        while queue:
            a, b = queue.popleft()
            if a + b == target or a == target or b == target:
                return True

            nxt = []

            # fill
            nxt.append((x, b))
            nxt.append((a, y))
            # empty
            nxt.append((0, b))
            nxt.append((a, 0))
            # pour a -> b
            pour = min(a, y - b)
            nxt.append((a - pour, b + pour))
            # pour b -> a
            pour = min(b, x - a)
            nxt.append((a + pour, b - pour))

            for s in nxt:
                if s not in seen:
                    seen.add(s)
                    queue.append(s)
        
        return False



