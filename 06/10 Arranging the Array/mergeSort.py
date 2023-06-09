from typing import List


class Solution:
    def Rearrange(self, n: int, arr: List[int]) -> None:
        self.sort(0, n, arr)

    def sort(self, start, end, arr):
        if end - start == 1:
            return

        middle = (start + end + 1) // 2
        self.sort(start, middle, arr)
        self.sort(middle, end, arr)

        l = start
        while l < middle and arr[l] < 0:
            l += 1
        self.reverse(l, middle, arr)

        r = middle
        while r < end and arr[r] < 0:
            r += 1
        self.reverse(middle, r, arr)

        self.reverse(l, r, arr)

    def reverse(self, start, end, arr):
        end -= 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


nums = [7, -6, 4, 5, -6, 7, 3, 5, -3]
Solution().Rearrange(len(nums), nums)
print(nums)
