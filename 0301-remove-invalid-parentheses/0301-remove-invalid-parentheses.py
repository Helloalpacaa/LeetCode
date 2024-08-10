class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def getMinRemove(s: str) -> int:
            left, right = 0, 0
            for i in range(len(s)):
                if s[i] == "(":
                    left += 1
                elif s[i] == ")":
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            
            return left + right
        
        def isValid(s: str) -> bool:
            left, right = 0, 0
            for i in range(len(s)):
                if s[i] == "(":
                    left += 1
                elif s[i] == ")":
                    if left > 0:
                        left -= 1
                    else:
                        return False
            return left == 0
        
        min_removal = getMinRemove(s)
        visited = set()
        queue = deque()
        queue.append(s)
        level = 0

        while queue:
            if level == min_removal:
                return [x for x in queue if isValid(x)]

            for _ in range(len(queue)):
                curr = queue.popleft()
                for i in range(len(curr)):
                    new_str = curr[:i] + curr[i+1:]
                    if new_str not in visited:
                        queue.append(new_str)
                    visited.add(new_str)
            
            level += 1

        return [""]
