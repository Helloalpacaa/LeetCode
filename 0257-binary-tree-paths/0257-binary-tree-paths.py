# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        
        ans = []
        path = ""
        self.traversal(root, path, ans)
        return ans
    
    def traversal(self, node: Optional[TreeNode], path: str, ans: List[str]) -> None:
        if node.left is None and node.right is None:
            ans.append(path + str(node.val))
            return
        
        if node.left:
            self.traversal(node.left, path + str(node.val) + "->", ans)
        if node.right:
            self.traversal(node.right, path + str(node.val) + "->", ans)
        