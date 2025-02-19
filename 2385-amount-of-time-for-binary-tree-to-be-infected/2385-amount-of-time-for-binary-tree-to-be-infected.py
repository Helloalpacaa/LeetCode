# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Build graph
        graph = defaultdict(list)

        def buildGraph(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
            if node is None:
                return

            graph[parent.val].append(node.val)
            graph[node.val].append(parent.val)

            buildGraph(node.left, node)
            buildGraph(node.right, node)
        
        buildGraph(root.left, root)
        buildGraph(root.right, root)
        print(graph)

        queue = deque([start])
        visited = set([start])
        time = -1

        while queue:
            time += 1
            for _ in range(len(queue)):
                current = queue.popleft()

                for adjacent in graph[current]:
                    if adjacent not in visited:
                        queue.append(adjacent)
                        visited.add(adjacent)
            
        return time