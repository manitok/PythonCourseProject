"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        value=postorder[-1]
        root=TreeNode(value)
        index=inorder.index(value)
        root.left=self.buildTree(inorder[:index],postorder[:index])
        root.right=self.buildTree(inorder[index+1:],postorder[index:-1])
        return root
        