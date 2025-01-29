class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        courseList = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course] += 1
            courseList[pre].append(course)
        
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        ans = []

        while queue:
            pre = queue.popleft()
            ans.append(pre)

            for course in courseList[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return ans