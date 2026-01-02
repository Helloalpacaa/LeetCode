class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Tree: every node has up to 1 indegree, root has 0 indegree
        indegree = defaultdict(int)
        adj = defaultdict(list)

        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
                adj[i].append(leftChild[i])
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
                adj[i].append(rightChild[i])

        for i in range(n):
            if indegree[i] > 1:
                return False
        
        rootCount = sum(1 for i in range(n) if indegree[i] == 0)
        if rootCount != 1:
            return False
        
        # Circle check
        root = next(i for i in range(n) if indegree[i] == 0)
        status = [0] * n # 0: not visited, 1: visiting, 2: visited

        def dfs(node):
            if status[node] == 2:
                return True
            
            if status[node] == 1:
                return False
            
            status[node] = 1
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            
            status[node] = 2
            return True
        
        dfs(root)
        return all(status[node] == 2 for node in range(n))


