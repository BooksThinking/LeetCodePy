"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        length_half = len(grid[0]) / 2
        temp_sum = 0
        for i, row in enumerate(grid):
            for j, number in enumerate(row):
                temp_sum += number
        if temp_sum == len(grid):
            return Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        elif temp_sum == 0:
            return Node(val=0, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        else:
            grid_tl = []
            grid_tr = []
            grid_bl = []
            grid_br = []
            for i, row in enumerate(grid):
                if i < length_half:
                    grid_tl.append(row[0:length_half])
                    grid_tr.append(row[length_half:len(grid[0])])
                else:
                    grid_bl.append(row[0:length_half])
                    grid_br.append(row[length_half:len(grid[0])])
            return Node(val=10, isLeaf=False, topLeft=Solution.construct(grid_tl), topRight=Solution.construct(grid_tr), bottomLeft=Solution.construct(grid_bl), bottomRight=Solution.construct(grid_br))
