# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = defaultdict(list)

        def buildGraph(child: TreeNode, parent: TreeNode) -> None:
            if child is None:
                return
            
            if parent:
                self.graph[child].append(parent)
                self.graph[parent].append(child)
            
            buildGraph(child.left, child)
            buildGraph(child.right, child)
        
        buildGraph(root, None)
        queue = deque([(target, 0)])
        visited = set([target])
        ans = []
        
        while queue:
            node, distance = queue.popleft()

            if distance == k:
                ans.append(node.val)

            for neighbor in self.graph[node]:
                if neighbor not in visited and distance < k:
                    visited.add(neighbor)
                    queue.append([neighbor, distance + 1])
        
        return ans
        




                
