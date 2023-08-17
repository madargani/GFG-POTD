class Solution:
    def generateNextPalindrome(self, num, n):
        if sum(num) == 9 * n:
            return [1] + [0] * (n - 1) + [1]
        
        for i in reversed(range(n)):
            if num[i] != 9:
                num[i] += 1
                break
            num[i] = 0
            
        front = num[0: n // 2]
        back = num[(n + 1) // 2: n]
        if list(reversed(front)) < back:
            middle = (n - 1) // 2
            for i in range(middle, -1, -1):
                if num[i] != 9:
                    num[i] += 1
                    break
                num[i] = 0
                
        for i in range(n // 2):
            num[-i - 1] = num[i]
            
        return num

num = [1, 2, 3, 4, 5, 6, 7]
print(Solution().generateNextPalindrome(num, len(num)))