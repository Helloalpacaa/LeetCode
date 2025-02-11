# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # arr = []
        # self.ans = None
        
        # def traverse(node: Optional) -> None:
        #     if node is None or self.ans is not None:
        #         return
            
        #     traverse(node.left)
        #     arr.append(node.val)
        #     if len(arr) == k:
        #         self.ans = arr[-1]
        #         return
        #     traverse(node.right)
        
        # traverse(root)
        # return self.ans

        stack = []
        arr = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
        
            root = stack.pop()
            k -= 1
            if k == 0:
                break
            arr.append(root.val)
            root = root.right
        
        return root.val
