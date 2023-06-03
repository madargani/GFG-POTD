class Solution:
    def isWordExist(self, board, word):
        def dfs(x, y, board, word):
            if not word:
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            if board[x][y] != word[0]:
                return False
            board[x][y] = ""
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if dfs(x + dx, y + dy, board, word[1:]):
                    return True
            board[x][y] = word[0]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, board, word):
                    return True
        return False


board = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(Solution().isWordExist(board, "abcf"))
