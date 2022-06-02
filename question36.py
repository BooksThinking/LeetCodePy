from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        row = [[0 for i in range(length)] for j in range(length)]
        colum = [[0 for i in range(length)] for j in range(length)]
        square = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if not tmp.isdigit():
                    continue
                if tmp in row[i]:
                    return False
                if tmp in colum[j]:
                    return False
                if tmp in square[(j // 3) * 3 + (i // 3)]:
                    return False
                row[i].append(tmp)
                colum[j].append(tmp)
                square[(j // 3) * 3 + (i // 3)].append(tmp)
        return True

board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
s = Solution()
print(s.isValidSudoku(board))