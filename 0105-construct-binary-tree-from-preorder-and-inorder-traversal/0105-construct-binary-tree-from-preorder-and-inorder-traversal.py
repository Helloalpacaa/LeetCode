# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hashmap -> val in preorder: index in inorder
        getIndex = {num: i for i, num in enumerate(inorder)}
        n = len(preorder)

        # find root
        # the first element in preorder is always the root, then find its place in inorder, left part is
        # its left child, right part is its right child
        def findRoot(preorderStart: int, preorderEnd: int, inorderStart: int, inorderEnd: int):
            if preorderStart > preorderEnd or inorderStart > inorderEnd:
                return None

            rootVal = preorder[preorderStart]
            index = getIndex[rootVal]
            leftLength = index - inorderStart
            rightLength = inorderEnd - index
            # print(rootVal, leftLength, rightLength, preorderStart, preorderEnd, inorderStart, inorderEnd)

            root = TreeNode(rootVal)
            root.left = findRoot(preorderStart + 1, preorderStart + leftLength, inorderStart, index - 1)
            root.right = findRoot(preorderStart + 1 + leftLength, preorderEnd, index + 1, inorderEnd)

            
            return root
        
        return findRoot(0, n - 1, 0, n - 1)
