class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        courseList = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            indegree[course] += 1
            courseList[pre].append(course)
        
        ans = []
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)

        while queue:
            pre = queue.popleft()
            ans.append(pre)
            for course in courseList[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return ans if len(ans) == numCourses else []

