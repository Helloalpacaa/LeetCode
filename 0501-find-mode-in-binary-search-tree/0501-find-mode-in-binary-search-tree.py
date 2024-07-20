# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.count = 0
        self.maxCount = 0
        self.pre = None
        
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            inorder(node.left)
            
            if self.pre is not None and self.pre.val != node.val:
                self.count = 1
            else:
                self.count += 1
            
            if self.count > self.maxCount:
                self.ans.clear()
                self.ans.append(node.val)
                self.maxCount = self.count
            elif self.count == self.maxCount:
                self.ans.append(node.val)
            
            self.pre = node
            inorder(node.right)
        
        inorder(root)
        
        return self.ans
        
        