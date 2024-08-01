# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.ans = []

        def traversal(node: Optional[TreeNode], isRoot: bool) -> TreeNode:
            if node is None:
                return None
            
            isDelete = node.val in to_delete
            if isRoot and not isDelete:
                self.ans.append(node)
            
            node.left = traversal(node.left, isDelete)
            node.right = traversal(node.right, isDelete)

            return None if isDelete else node
        
        root = traversal(root, True)
        return self.ans