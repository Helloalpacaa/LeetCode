# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def findRoot(preStart: int, preEnd: int, inStart: int, inEnd: int) -> Optional[TreeNode]:
            if preStart >= preEnd or inStart >= inEnd:
                return None
            
            rootValue = preorder[preStart]
            rootIdx = inorderMap[rootValue]
            leftLength = rootIdx - inStart
            
            root = TreeNode(rootValue)
            root.left = findRoot(preStart + 1, preStart + leftLength + 1, inStart, rootIdx)
            root.right = findRoot(preStart + leftLength + 1, preEnd, rootIdx + 1, inEnd)
            
            return root
            
        
        inorderMap = {val: idx for idx, val in enumerate(inorder)}
        
        return findRoot(0, len(preorder), 0, len(inorder))