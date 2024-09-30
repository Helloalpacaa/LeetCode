class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        ans = [i for i in range(numCourses) if indegree[i] == 0]

        for i in ans:
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    ans.append(j)
        
        return ans if len(ans) == numCourses else []