class Solution:
    def findPreSuc(self, root, pre, suc, key):
        # Find pre
        cur = root
        while True:
            if not cur:
                break
            if cur.key >= key:
                cur = cur.left
            else:
                pre = cur
                cur = cur.right

        # Find suc
        cur = root
        while True:
            if not cur:
                break
            if cur.key <= key:
                cur = cur.right
            else:
                suc = cur
                cur = cur.left
