from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        length = len(grid)
        sum1 = 0


        sum2 = 0
        sum1_array = [0]
        sum1_array = sum1_array * length
        for i , data in enumerate(grid):
            max = 0
            for data_number in data:
                if data_number > 0:
                    sum1 = sum1 + 1
                if data_number > max:
                    max = data_number
            sum1_array[i] = max
        for count in sum1_array:
            sum2 += count

        sum3 = 0
        sum3_array = [0]
        sum3_array = sum3_array * length
        for i in range(0 ,length):
            max_number = 0
            for data in grid:
                if data[i] > max_number:
                    max_number = data[i]
            sum3_array[i] = max_number
        for count2 in sum3_array:
            sum3 += count2
        return sum1 + sum2 + sum3

