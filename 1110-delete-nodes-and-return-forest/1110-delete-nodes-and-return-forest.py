# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.deleteLists = set(to_delete)
        self.ans = []

        def traversal(node: Optional[TreeNode], isRoot: bool) -> Optional[TreeNode]:
            if node is None:
                return None
            
            isDelete = node.val in self.deleteLists
            # 只有当遇到新的root且不在被删除list里才需要加进ans里
            if isRoot and not isDelete:
                self.ans.append(node)
            
            # 如果isDelete为True，那么它的children就是新的root
            node.left = traversal(node.left, isDelete)
            node.right = traversal(node.right, isDelete)

            return None if isDelete else node
        
        traversal(root, True)
        return self.ans
