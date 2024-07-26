# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = self.dfs(root, 0)
    
    def dfs(self, node: Optional[TreeNode], val: int):
        if node is None:
            return
        
        node.val = val
        node.left = self.dfs(node.left, node.val * 2 + 1)
        node.right = self.dfs(node.right, node.val * 2 + 2)

        return node

    def find(self, target: int) -> bool:
        return self.findHelper(self.root, target)
    
    def findHelper(self, node: Optional[TreeNode], target: int) -> bool:
        if node is None:
            return False
        
        if node.val == target:
            return True

        if node.val > target:
            return False
        
        return self.findHelper(node.left, target) or self.findHelper(node.right, target)
        

        
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)