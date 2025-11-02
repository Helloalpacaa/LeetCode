class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course, pre in prerequisites:
            indegree[course] += 1
            graph[pre].append(course)
        
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        res = []

        while queue:
            curr = queue.popleft()
            res.append(curr)

            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return res if len(res) == numCourses else []