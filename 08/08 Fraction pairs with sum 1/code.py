from math import gcd
from collections import Counter

class Solution:
    def countFractions(self, n, numerator, denominator):
        fractions = []
        for i in range(n):
            factor = gcd(numerator[i], denominator[i])
            fractions.append((numerator[i] // factor, denominator[i] // factor))
        
        freqs = Counter(fractions)
        
        count = 0
        for fract, freq in freqs.items():
            target = (fract[1] - fract[0], fract[1])
            if target in freqs:
                count += freq * freqs[target]
        if (1, 2) in freqs:
            count -= freqs[(1, 2)]
                
        return count // 2


numerator = [3, 1, 12, 81, 2, 1, 1]
denominator = [9, 10, 18, 90, 5, 2, 2] 
N = len(numerator)      
count = Solution().countFractions(N, numerator, denominator)
print(count)