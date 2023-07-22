class Solution:
    def removeDuplicates(self, head):
        seen = set()
        
        cur = head
        seen.add(cur.data)
        
        while cur.next:
            if cur.next.data in seen:
                cur.next = cur.next.next
            else:
                cur = cur.next
                seen.add(cur.data)
                
        return head