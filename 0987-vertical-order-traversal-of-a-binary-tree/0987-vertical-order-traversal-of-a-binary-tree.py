# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0, 0)])
        nodes = defaultdict(list)

        while queue:
            node, row, col = queue.popleft()
            nodes[col].append((row, node.val))

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        res = []
        for col in sorted(nodes.keys()):
            sorted_nodes = sorted(nodes[col], key=lambda x: (x[0], x[1]))
            res.append([val for _, val in sorted_nodes])
        
        return res
