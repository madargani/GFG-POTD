class Solution:
    def sortByFreq(self,arr):
        freqs = [0] * (max(arr) + 1)
        for i in arr:
            freqs[i] += 1
        arr.sort(key=lambda x: (-freqs[x], x))
        return arr

