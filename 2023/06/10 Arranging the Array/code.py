from typing import List


class Solution:
    def Rearrange(self, n: int, arr: List[int]) -> None:
        neg = []
        pos = []
        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        index = 0
        for i in neg:
            arr[index] = i
            index += 1
        for i in pos:
            arr[index] = i
            index += 1
