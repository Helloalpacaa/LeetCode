class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preList = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            preList[course].append(pre)

        exploring = set()
        visited = set()

        def dfs(course) -> bool:
            if course in exploring:
                return True
            
            if course in visited:
                return False
            
            exploring.add(course)
            
            for pre in preList[course]:
                if dfs(pre):
                    return True
            
            exploring.remove(course)
            visited.add(course)

            return False
            


        for course, pre in prerequisites:
            if dfs(course):
                return False
        
        return True