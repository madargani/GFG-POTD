class Solution:
    def segregate(self, head):
        freqs = [0] * 3
        
        cur = head
        while cur:
            freqs[cur.data] += 1
            cur = cur.next
        
        cur = head
        i = 0
        while cur:
            while freqs[i] <= 0:
                i += 1
            cur.data = i
            freqs[i] -= 1
            cur = cur.next
            
        return head