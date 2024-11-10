# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. build a hashmap of (value, index) pair of inorder
        hashmap = {}
        for idx, val in enumerate(inorder):
            hashmap[val] = idx
        
        # 2. find the root of each sub tree
        def findRoot(preStart, preEnd, inStart, inEnd) -> TreeNode:
            # base case:
            if preStart > preEnd or inStart > inEnd:
                return None

            # Create the root node
            rootVal = preorder[preStart]
            root = TreeNode(rootVal)
            # find the index of root in inorder
            rootIdx = hashmap[rootVal]
            # find the length of the left sub tree
            length = rootIdx - inStart

            root.left = findRoot(preStart + 1, preStart + length, inStart, rootIdx - 1)
            root.right = findRoot(preStart + length + 1, preEnd, rootIdx + 1, inEnd)

            return root
        
        return findRoot(0, len(preorder) - 1, 0, len(inorder) - 1)

