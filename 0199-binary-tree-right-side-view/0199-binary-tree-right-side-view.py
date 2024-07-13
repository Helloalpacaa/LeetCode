# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traversal(root, ans, 0)
        return ans
    
    def traversal(self, node: Optional[TreeNode], ans: List[int], height: int) -> None:
        if node is None:
            return
        
        if height >= len(ans):
            ans.append(node.val)
        
        self.traversal(node.right, ans, height + 1)
        self.traversal(node.left, ans, height + 1)