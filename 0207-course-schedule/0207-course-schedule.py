class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS
        # graph = defaultdict(list)
        # for course, pre in prerequisites:
        #     graph[pre].append(course)
        
        # status = [0] * numCourses # 0: not explored, 1: exploring, 2: explored
        
        # def dfs(course) -> bool:
        #     if status[course] == 1:
        #         return False
            
        #     if status[course] == 2:
        #         return True
            
        #     status[course] = 1
        #     for nxt in graph[course]:
        #         if not dfs(nxt):
        #             return False
            
        #     status[course] = 2
        #     return True
        
        # for course, pre in prerequisites:
        #     if status[pre] == 0:
        #         if not dfs(pre):
        #             return False
        
        # return True

        # Topological Sort
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course, pre in prerequisites:
            indegree[course] += 1
            graph[pre].append(course)
        
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        total = 0
        while queue:
            curr = queue.popleft()
            total += 1

            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return total == numCourses

