# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 建一个graph, 连接每个node和它的邻居，比如node1：3,0,8
        def buildGraph(child: TreeNode, parent: TreeNode) -> None:
            if not child:
                return

            if parent:
                self.graph[child].append(parent)
                self.graph[parent].append(child)
            
            buildGraph(child.left, child)
            buildGraph(child.right, child)

        self.graph = defaultdict(list)
        buildGraph(root, None)

        queue = deque([(target, 0)])
        visited = set([target])
        result = []

        while queue:
            node, distance = queue.popleft()

            if distance == k:
                result.append(node.val)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited and distance < k:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        
        return result

