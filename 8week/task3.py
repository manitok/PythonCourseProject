"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        level = 0
        queue = deque()
        queue.append([root])
        while queue:
            prev_level_nodes = queue.pop()
            if level % 2 == 1:
                result.append([node.val for node in prev_level_nodes[::-1]])
            else:
                result.append([node.val for node in prev_level_nodes])

            level += 1
            current_level_nodes = []
            for node in prev_level_nodes:
                if node.left is not None:
                    current_level_nodes.append(node.left)
                if node.right is not None:
                    current_level_nodes.append(node.right)
            if current_level_nodes:
                queue.append(current_level_nodes)
        return result
            