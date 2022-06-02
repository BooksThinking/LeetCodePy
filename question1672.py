from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for row in accounts:
            sum = 0
            for colum in row:
                sum = sum + colum
            if sum > max:
                max = sum
        return max