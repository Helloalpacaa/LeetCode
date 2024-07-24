# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 建一个hashmap，找到从root到target的沿路的node到target的距离，例子一的hashmap里就只会有3和5
        def find(node: TreeNode) -> int:
            if node is None:
                return -1

            if node == target:
                self.hm[node] = 0
                return 0
            
            left = find(node.left)
            if left >= 0:
                self.hm[node] = left + 1
                return left + 1
            
            right = find(node.right)
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

        self.hm = {}
        find(root)
        self.ans = []
        dfs(root, self.hm[root])

        return self.ans
