# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count = 0
        self.maxCount = 0
        self.ans = []
        self.pre = None

        def traversal(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            traversal(node.left)

            if self.pre is not None and node.val == self.pre.val:
                self.count += 1
            else:
                self.count = 1
            
            self.pre = node
            
            if self.count > self.maxCount:
                self.maxCount = self.count
                self.ans.clear()
                self.ans.append(node.val)
            elif self.count == self.maxCount:
                self.ans.append(node.val)
            
            traversal(node.right)
        
        traversal(root)
        return self.ans

            
