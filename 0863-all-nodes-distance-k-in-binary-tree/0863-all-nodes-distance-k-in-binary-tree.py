# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.hm = {}
        self.ans = []

        def build(node: TreeNode) -> int:
            if node is None:
                return -1
            
            if node == target:
                self.hm[node] = 0
                return 0
            
            left = build(node.left)
            if left >= 0:
                self.hm[node] = left + 1
                return left + 1
            
            right = build(node.right)
            if right >= 0:
                self.hm[node] = right + 1
                return right + 1
            
            return -1
        
        def dfs(node: TreeNode, length: int) -> None:
            if node is None:
                return
            
            if node in self.hm:
                length = self.hm[node]

            if length == k:
                self.ans.append(node.val)
            
            dfs(node.left, length + 1)
            dfs(node.right, length + 1)
        
        build(root)
        dfs(root, self.hm[root])
        return self.ans
                
