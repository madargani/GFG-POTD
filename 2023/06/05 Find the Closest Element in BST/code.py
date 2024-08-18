import sys


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def minDiff(self, root, K):
        if K < root.data:
            if root.left:
                return min(root.data - K, self.minDiff(root.left, K))
            return root.data - K
        if K > root.data:
            if root.right:
                return min(K - root.data, self.minDiff(root.right, K))
            return K - root.data
        return 0

        # 1 x 3  5
