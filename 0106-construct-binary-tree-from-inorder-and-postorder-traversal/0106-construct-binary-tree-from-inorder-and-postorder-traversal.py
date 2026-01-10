# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        getIndex = {num: index for index, num in enumerate(inorder)}
        n = len(inorder)

        def getRoot(inStart, inEnd, posStart, posEnd):
            if inStart > inEnd or posStart > posEnd:
                return None

            rootVal = postorder[posEnd]
            index = getIndex[rootVal]
            left = index - inStart
            right = inEnd - index

            root = TreeNode(rootVal)
            root.left = getRoot(inStart, inStart + left - 1, posStart, posStart + left - 1)
            root.right = getRoot(index + 1, index + right, posStart + left, posEnd - 1)

            return root
        
        return getRoot(0, n - 1, 0, n - 1)
