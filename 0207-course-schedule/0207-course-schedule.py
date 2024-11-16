class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseList = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            courseList[course].append(pre)
        
        exploring = set()
        visited = set()

        def dfs(course) -> bool:
            if course in exploring:
                return False
            
            if course in visited:
                return True

            exploring.add(course)

            for pre in courseList[course]:
                if not dfs(pre):
                    return False
            
            exploring.remove(course)
            visited.add(course)

            return True
        
        for course, pre in prerequisites:
            if not dfs(course):
                return False
        
        return True