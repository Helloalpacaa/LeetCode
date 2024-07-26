class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        self.diameter = 0
        
        def traversal(parent: Optional[TreeNode], child: Optional[TreeNode]) -> int:
            firstLongest, secondLongest = 0, 0
            for neighbor in graph[child]:
                if neighbor != parent:
                    length = traversal(child, neighbor)
                    if length > firstLongest:
                        firstLongest, secondLongest = length, firstLongest
                    elif length > secondLongest:
                        secondLongest = length
                    self.diameter = max(self.diameter, firstLongest + secondLongest)
            
            return firstLongest + 1
        
        traversal(None, 0)
        return self.diameter