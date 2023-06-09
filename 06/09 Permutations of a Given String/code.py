class Solution:
    def find_permutation(self, S):
        perms = set()
        self.heaps_alg([c for c in S], len(S), perms)
        return sorted(perms)

    def heaps_alg(self, a, size, perms):
        if size == 1:
            perms.add("".join(a))
            return a

        for i in range(size):
            self.heaps_alg(a, size - 1, perms)
            if size & 1:
                a[0], a[size - 1] = a[size - 1], a[0]
            else:
                a[i], a[size - 1] = a[size - 1], a[i]


print(Solution().find_permutation("ABC"))
