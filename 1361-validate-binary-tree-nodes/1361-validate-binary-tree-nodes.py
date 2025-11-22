class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        adj = defaultdict(list)

        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]

            if left != -1:
                indegree[left] += 1
                if indegree[left] > 1:
                    return False
                adj[i].append(left)
            if right != -1:
                indegree[right] += 1
                if indegree[right] > 1:
                    return False
                adj[i].append(right)
        
        root = [indegree[i] for i in range(n) if indegree[i] == 0]
        if len(root) != 1:
            return False
        r = root[0]

        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False
            
            if state[node] == 2:
                return True

            state[node] = 1
            for child in adj[node]:
                if not dfs(child):
                    return False
            
            state[node] = 2
            return True
        
        for i in range(n):
            if not dfs(i):
                print(i)
                return False
        
        return True
        
            

            

