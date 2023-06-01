def LargButMinFreq(arr,n):
    freqs = {}
    for num in arr:
        if not num in freqs:
            freqs[num] = 0
        freqs[num] += 1
        
    ans = -1
    min_freq = n + 1
    for num, freq in freqs.items():
        if freq < min_freq:
            ans = num
            min_freq = freq
        elif freq == min_freq:
            if num > ans:
                ans = num

    return ans

print(LargButMinFreq([3, 3, 5, 5], 4))

