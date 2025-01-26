class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        courseList = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            indegree[course] += 1
            courseList[pre].append(course)
        
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])

        while queue:
            pre = queue.popleft()
            completed += 1
            for course in courseList[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return all(indegree[course] == 0 for course in range(numCourses))