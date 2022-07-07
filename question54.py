class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        '''
        direction表示方向
        1表示向右
        2表示向下
        3表示向左
        4表示向上
        '''
        direction = 1
        count, row, colum = 0, 0, 0
        row__length = len(matrix)
        colum__length = len(matrix[0])
        sum = row__length * colum__length
        while count < sum:
            count += 1
            result.append(matrix[row][colum])
            matrix[row][colum] = 0
            if direction == 1:
                if colum == colum__length-1 or matrix[row][colum+1] == 0:
                    direction = 2
                    row += 1
                else:
                    colum += 1
            elif direction == 2:
                if row == row__length-1 or matrix[row+1][colum] == 0:
                    direction = 3
                    colum -= 1
                else:
                    row += 1
            elif direction == 3:
                if colum == 0 or matrix[row][colum-1] == 0:
                    direction = 4
                    row -= 1
                else:
                    colum -= 1
            else:
                if row == 0 or matrix[row-1][colum] == 0:
                    direction = 1
                    colum += 1
                else:
                    row -= 1
        return result

s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))