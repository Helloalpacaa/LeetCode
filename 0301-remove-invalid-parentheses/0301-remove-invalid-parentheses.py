class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []

        def isValid(s: str) -> bool:
            count = 0
            for char in s:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                
                # 说明有一个“）”前面没有对应的“（”
                if count < 0:
                    return False
            
            # 遍历完S后，count需要等于0
            return count == 0
        
        def getMinRemoval(s: str) -> int:
            left = right = 0
            for char in s:
                if char == "(":
                    left += 1
                elif char == ")":
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            
            return left + right
        
        # BFS
        min_removal = getMinRemoval(s)
        queue = deque([s])
        visited = set([s]) # 去重
        level = 0 # 用来记录已经移除了多少个char

        while queue:
            if level == min_removal:
                return [x for x in queue if isValid(x)]
            
            for _ in range(len(queue)):
                curr = queue.popleft() # get the string, example - "()())()"
                for i in range(len(curr)):
                    if curr[i] in '()':
                        new_str = curr[:i] + curr[i+1:]
                        # 不能在这里check是否valid，因为有可能先加入一个invalid的str，再通过删除变成valid
                        if new_str not in visited:
                            queue.append(new_str)
                            visited.add(new_str)
            
            level += 1
        
        return [""]


        

        
