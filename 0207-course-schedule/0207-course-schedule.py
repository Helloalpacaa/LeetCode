class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        status = [0] * numCourses # 0: not explored, 1: exploring, 2: explored
        
        def dfs(course) -> bool:
            if status[course] == 1:
                return False
            
            if status[course] == 2:
                return True
            
            status[course] = 1
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            
            status[course] = 2
            return True
        
        for course, pre in prerequisites:
            if not dfs(pre):
                return False
        
        return True
