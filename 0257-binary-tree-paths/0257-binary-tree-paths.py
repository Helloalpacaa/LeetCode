# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traversal(node: Optional[TreeNode], path: str) -> None:
            if node.left is None and node.right is None:
                self.ans.append(path)
                return
            
            if node.left:
                traversal(node.left, path + "->" + str(node.left.val))
            if node.right:
                traversal(node.right, path + "->" + str(node.right.val))
        
        self.ans = []
        traversal(root, str(root.val))
        return self.ans