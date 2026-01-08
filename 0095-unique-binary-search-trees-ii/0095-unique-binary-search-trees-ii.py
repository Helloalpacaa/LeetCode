# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build(left, right):
            if left > right:
                return [None]
            
            res = []
            for root in range(left, right + 1):
                leftNodes = build(left, root - 1)
                rightNodes = build(root + 1, right)

                for l in leftNodes:
                    for r in rightNodes:
                        r = TreeNode(root, l, r)
                        res.append(r)
            
            return res
        
        return build(1, n)



