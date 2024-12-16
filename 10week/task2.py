"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/path-sum-ii/description/
"""
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, total = 0, path = []):
            if not node: return
            path.append(node.val)
            total += node.val
            if not (node.left or node.right) and total == targetSum:
                paths.append(list(path))
            else:
                dfs(node.left, total), dfs(node.right, total)
            total -= path.pop()
        paths = []
        dfs(root)
        return paths