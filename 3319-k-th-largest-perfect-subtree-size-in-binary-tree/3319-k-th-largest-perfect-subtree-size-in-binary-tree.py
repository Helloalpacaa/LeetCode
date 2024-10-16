# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_subtrees = []

        def dfs(node: Optional[TreeNode]) -> (int, int, bool):
            if node is None:
                return (0, 0, True)
            
            leftDegree, left_perfect_subtree, is_left_perfect_subtree = dfs(node.left)
            rightDegree, right_perfect_subtree, is_right_perfect_subtree = dfs(node.right)

            if leftDegree == rightDegree and is_left_perfect_subtree and is_right_perfect_subtree:
                perfect_subtree = left_perfect_subtree + right_perfect_subtree + 1
                perfect_subtrees.append(perfect_subtree)
                return (leftDegree + 1, perfect_subtree, True)
            else:
                return (max(leftDegree, rightDegree) + 1, 0, False)
        
        
        dfs(root)
        print(perfect_subtrees)
        perfect_subtrees.sort(reverse=True)
        return -1 if len(perfect_subtrees) < k else perfect_subtrees[k - 1]