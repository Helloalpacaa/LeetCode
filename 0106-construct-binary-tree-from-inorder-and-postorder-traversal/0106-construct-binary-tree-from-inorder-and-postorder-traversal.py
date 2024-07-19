# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def findRoot(inorderStart: int, inorderEnd: int, postorderStart: int, postorderEnd: int) -> TreeNode:
            if inorderStart >= inorderEnd or postorderStart >= postorderEnd:
                return None
            
            rootValue = postorder[postorderEnd - 1]
            rootIndex = inorderMap[rootValue]
            leftLength = rootIndex - inorderStart
            
            root = TreeNode(rootValue)
            root.left = findRoot(inorderStart, rootIndex, postorderStart, postorderStart + leftLength)
            root.right = findRoot(rootIndex + 1, inorderEnd, postorderStart + leftLength, postorderEnd - 1)
            return root
            
    
        inorderMap = {val: idx for idx, val in enumerate(inorder)}
        
        return findRoot(0, len(inorder), 0, len(postorder))
        
        