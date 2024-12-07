"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        dct = {}
        for i in range(len(inorder)):
            dct[inorder[i]] = i

        def dfs(l, r):
            nonlocal preorder_index
            if l > r:
                return None
            root = TreeNode(preorder[preorder_index])
            mid = dct[preorder[preorder_index]]
            preorder_index = preorder_index + 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)