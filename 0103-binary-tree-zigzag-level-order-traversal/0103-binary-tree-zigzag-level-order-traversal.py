# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def traversal(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            
            if len(ans) < depth:
                ans.append([])
            
            if depth % 2 == 1:
                ans[depth - 1].append(node.val)
            else:
                ans[depth - 1].insert(0, node.val)

            traversal(node.left, depth + 1)
            traversal(node.right, depth + 1)
        
        traversal(root, 1)
        return ans