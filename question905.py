from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pointer1 = 0
        pointer2 = len(nums)-1
        while pointer1 < pointer2:
            while(nums[pointer1] % 2 == 0 and pointer1 < pointer2):
                pointer1 += 1
            while(nums[pointer2] % 2 == 1 and pointer1 < pointer2):
                pointer2 -= 1
            if pointer1 < pointer2:
                temp = nums[pointer1]
                nums[pointer1] = nums[pointer2]
                nums[pointer2] = temp
        return nums

a = [0,2]
s = Solution()
print(s.sortArrayByParity(a))