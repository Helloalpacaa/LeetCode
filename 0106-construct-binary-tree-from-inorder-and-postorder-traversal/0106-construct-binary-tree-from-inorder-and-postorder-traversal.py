# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def findRoot(inStart, inEnd, postStart, postEnd) -> Optional[TreeNode]:
            if inStart >= inEnd or postStart >= postEnd:
                return None
            
            rootValue = postorder[postEnd - 1]
            rootIdx = self.inorderMap[rootValue]
            leftLength = rootIdx - inStart

            root = TreeNode(rootValue)
            root.left = findRoot(inStart, rootIdx, postStart, postStart + leftLength)
            root.right = findRoot(rootIdx + 1, inEnd, postStart + leftLength, postEnd - 1)

            return root
        
        self.inorderMap = {val: idx for idx, val in enumerate(inorder)}

        return findRoot(0, len(inorder), 0, len(postorder))