"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
"""
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def divideFromMiddle(head) :
            if head is None or head.next is None : return None, head
            fast, slow = head.next.next, head
            while fast and fast.next :
                fast = fast.next.next
                slow = slow.next
            head2 = slow.next
            slow.next = None
            return head, head2

        def helper(head) :
            if not head : return None
            lPart, rPart = divideFromMiddle(head)
            root = TreeNode(rPart.val)
            root.left, root.right = helper(lPart), helper(rPart.next)
            return root

        return helper(head)