class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set([0])
        queue = deque([0])

        while queue:
            index = queue.popleft()
            for room in rooms[index]:
                if room not in visited:
                    queue.append(room)
                    visited.add(room)

        return len(visited) == n