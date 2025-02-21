# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def buildgraph(child: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
            if child is None:
                return
            
            if parent:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)

            buildgraph(child.left, child)
            buildgraph(child.right, child)
        
        buildgraph(root, None)

        queue = deque([start])
        visited = set([start])
        minutes = -1

        while queue:
            for _ in range(len(queue)):
                current_val = queue.popleft()
                
                for adj in graph[current_val]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
            
            minutes += 1
        
        return minutes


