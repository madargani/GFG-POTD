class Solution:
    def reverseEqn(self, s):
        tokens = []
        i = 0
        while i < len(s):
            token = s[i]
            if not s[i].isdigit():
                tokens.append(token)
                i += 1
                continue

            i += 1
            while i < len(s) and s[i].isdigit():
                token += s[i]
                i += 1
            tokens.append(token)

        tokens.reverse()
        return "".join(tokens)


print(Solution().reverseEqn("1+23-456*7"))
