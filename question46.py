import copy
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return randomSort(nums)

def randomSort(nums: list[int]) -> list[list[int]]:
    result = []
    if len(nums) == 1:
        temp = [nums[0]]
        result.append(temp)
        return result
    nextResult = randomSort(nums[1:])
    for data in nextResult:
        for i in range(0, len(data) + 1):
            temp = copy.deepcopy(data)
            temp.insert(i, nums[0])
            result.append(temp)
    return result



s = Solution()
print(s.permute([1, 2, 3]))