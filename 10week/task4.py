"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Use bfs
        que = deque()
        que.append(root)
        while que and que[0]:
            length = len(que)
            for i in range(length):
                curr = que.popleft()
                curr.next = que[0] if i+1 < length else None
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                
        return root