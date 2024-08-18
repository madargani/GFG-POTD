class Solution:
    def longestSubsequence(self,a,n):
        table = []
        
        for num in a:
            if not table or num > table[-1]:
                table.append(num)
            else:
                i = self.search(table, num)
                table[i] = num
                        
        return len(table)
    
    def search(self, table, num):
        l = 0 
        r = len(table) - 1
        while l < r:
            m = (l + r) // 2
            if table[m] >= num:
                r = m
            else:
                l = m + 1
        return l
            
    
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(Solution().longestSubsequence(arr, len(arr)))