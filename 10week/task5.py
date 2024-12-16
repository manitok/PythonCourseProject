class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append((root,0))
        res = []
        if not root:
            return res
        while queue:
            node,depth = queue.popleft()
            if node:
                if len(res) <= depth:
                    res.insert(0,[])
                
                res[-(depth+1)].insert(0,node.val)
                queue.insert(0,(node.left,depth+1))
                queue.insert(0,(node.right,depth+1))
            
        return res