from typing import List


class Solution:
    def maxEqualSum(self, N1: int, N2: int, N3: int, S1: List[int], S2: List[int], S3: List[int]) -> int:
        lists = [S1, S2, S3]
        for l in lists:
            l.reverse()

        sums = [sum(S1), sum(S2), sum(S3)]
        if sums[0] == sums[1] == sums[2]:
            return sums[0]

        while True:
            index = 0
            for i in range(1, 3):
                if sums[i] > sums[index]:
                    index = i

            sums[index] -= lists[index].pop()

            if sums[0] == sums[1] == sums[2]:
                return sums[0]


S1 = [4, 2, 3]
S2 = [1, 1, 2, 3]
S3 = [1, 4]

print(Solution().maxEqualSum(len(S1), len(S2), len(S3), S1, S2, S3))
