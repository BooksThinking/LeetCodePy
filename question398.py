import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.number_list = nums
        self.dict = {}
        count = 0
        for tempNumber in self.number_list:
            if tempNumber in self.dict.keys():
                val = self.dict.get(tempNumber)
                val.append(count)
                self.dict[tempNumber] = val
            else:
                self.dict[tempNumber] = [count]
            count = count + 1

    def pick(self, target: int) -> int:
        if target in self.dict.keys():
            val_set = self.dict[target]
            length = len(val_set)
            n = random.randint(0, length-1)
            return val_set[n]
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

solution = Solution([1, 2, 3, 3, 3]);
print(solution.pick(3))
print(solution.pick(1))
print(solution.pick(3))
