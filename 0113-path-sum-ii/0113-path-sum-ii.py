# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        if root is None:
            return self.paths
        
        self.traversal(root, root.val, targetSum, [root.val])
        
        return self.paths
    
    def traversal(self, node: Optional[TreeNode], total: int, targetSum: int, path: List[int]) -> None:
        if total == targetSum and node.left is None and node.right is None:
            self.paths.append(path[:]) # if you append path, then you are append the reference of the path, and the path is changing all the time, so you need to append a copy of the path
            return
        
        if node.left:
            total += node.left.val
            path.append(node.left.val)
            self.traversal(node.left, total, targetSum, path)
            total -= node.left.val
            path.pop()
        
        if node.right:
            total += node.right.val
            path.append(node.right.val)
            self.traversal(node.right, total, targetSum, path)
            total -= node.right.val
            path.pop()
        
            
        