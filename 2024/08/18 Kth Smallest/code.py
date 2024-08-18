class Solution:
    def kthSmallest(self, arr, k):
        seen = [False] * (max(arr) + 1)

        for i in arr:
            seen[i] = True

        for i, x in enumerate(seen):
            if not x:
                continue
            k -= 1
            if k == 0:
                return i

if __name__ == "__main__":
    arr = [7, 10, 4, 20, 15]
    k = 4
    res = Solution().kthSmallest(arr, k)
    print(res)
