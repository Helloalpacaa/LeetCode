# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def findRoot(start: int, end: int) -> Optional[TreeNode]:
            if start >= end:
                return None
            
            rootValue = preorder[start]
            leftEnd = start + 1
            while leftEnd < len(preorder) and preorder[leftEnd] < rootValue:
                leftEnd += 1
            
            root = TreeNode(rootValue)
            root.left = findRoot(start + 1, leftEnd)
            root.right = findRoot(leftEnd, end)
            
            return root
        
        return findRoot(0, len(preorder))