import copy
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        return randomSort(nums)

def randomSort(nums: list[int]) -> list[list[int]]:
    result = []
    if len(nums) == 1:
        temp = [nums[0]]
        result.append(temp)
        return result
    nextResult = randomSort(nums[1:])
    for data in nextResult:
        check = True
        for i in range(0, len(data)):
            if not check:
                continue
            temp = copy.deepcopy(data)
            temp.insert(i, nums[0])
            result.append(temp)
            if nums[0] != data[i]:
                check = True
            elif nums[0] == data[i] and check:
                check = False
        if check:
            temp = copy.deepcopy(data)
            temp.insert(len(data), nums[0])
            result.append(temp)
    return result


s = Solution()
print(s.permuteUnique([1, 1, 2]))