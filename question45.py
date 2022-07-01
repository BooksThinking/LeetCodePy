class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            return search(0, nums)

def search(begin: int, nums: list[int]) -> int:
    print(begin)
    if nums[begin] == 0:
        return -1
    if (begin + nums[begin]) >= len(nums) - 1:
        return 1
    next = begin
    min = 10000
    for next in range(begin + 1, begin + nums[begin] + 1):
         temp = search(next, nums)
         if temp == -1:
             print("????????")
             continue
         if temp + 1 < min:
             min = temp + 1
    return min

s = Solution()
nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
# print(nums[35])
print(s.jump(nums))
