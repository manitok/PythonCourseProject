"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees-ii/description/
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        ans=[]
        if root!=None:
            q.append(root)

        while len(q)>0:
            level=[]
            qlen=len(q)

            for _ in range(qlen):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)

                if node.right!=None:
                    q.append(node.right)


            ans.append(level)

        return ans