# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traversal(root, ans)
        return ans
    
    def traversal(self, node: Optional[TreeNode], ans: List[int]) -> None:
        if node is None:
            return
        
        self.traversal(node.left, ans)
        ans.append(node.val)
        self.traversal(node.right, ans)
    