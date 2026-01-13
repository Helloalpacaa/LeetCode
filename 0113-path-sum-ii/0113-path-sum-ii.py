# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        if not root:
            return res

        def traversal(node: Optional[TreeNode], total: int, path: List[int]) -> None:
            if total == targetSum and not node.left and not node.right:
                res.append(path[:])
                return
            
            if node.left:
                traversal(node.left, total + node.left.val, path + [node.left.val])
            if node.right:
                traversal(node.right, total + node.right.val, path + [node.right.val])
        
        traversal(root, root.val, [root.val])
        return res
