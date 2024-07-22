# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtracking(node: Optional[TreeNode], path: List[int], total) -> None:
            if total == targetSum:
                self.ans.append(path[:])
                return
            
            if node.left:
                backtracking(node.left, path + [node.left.val], total + node.left.val)
            if node.right:
                backtracking(node.right, path + [node.right.val], total + node.right.val)
        
        self.ans = []
        if root is None:
            return []
        backtracking(root, [root.val], root.val)
        return self.ans
            