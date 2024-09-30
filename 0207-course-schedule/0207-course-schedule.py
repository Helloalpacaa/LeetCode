class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS 解法
        # graph = [[] for _ in range(numCourses)]
        # for course, pre in prerequisites:
        #     graph[course].append(pre)
        
        # exploring = set()
        # visited = set()

        # def dfs(course) -> bool:
        #     if course in exploring:
        #         return True # 有环
            
        #     if course in visited:
        #         return False # 没有环
            
        #     exploring.add(course)

        #     for pre in graph[course]:
        #         if dfs(pre):
        #             return True # 有环
            
        #     # 没有遇到有环的情况，结束exploring，放进visited
        #     exploring.remove(course) 
        #     visited.add(course)

        #     return False
        
        # for course, pre in prerequisites:
        #     if dfs(pre):
        #         return False
        
        # return True

        # BFS解法
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        bfs = [i for i in range(numCourses) if indegree[i] == 0]

        for i in bfs:
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    bfs.append(j)
        
        return len(bfs) == numCourses
