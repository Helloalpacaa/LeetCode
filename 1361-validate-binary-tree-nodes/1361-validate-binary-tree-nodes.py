class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n

        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]

            if i == left or i == right:
                continue

            if left != -1:
                indegree[left] += 1
                if indegree[left] > 1:
                    return False

            if right != -1:
                indegree[right] += 1
                if indegree[right] > 1:
                    return False
        
        root = [i for i in range(n) if indegree[i] == 0]
        if len(root) != 1:
            return False
        
        r = root[0]
        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                print(node)
                return False
            
            if state[node] == 2:
                return True

            state[node] = 1
            if leftChild[node] != -1:
                if not dfs(leftChild[node]):
                    return False
            if rightChild[node] != -1:
                if not dfs(rightChild[node]):
                    return False
            
            state[node] = 2
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        
        return True
        
            

            

