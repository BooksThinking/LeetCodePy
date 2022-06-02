from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            if left == len(nums):
                return -1
            return left if nums[left] == target else -1

        def searchRight(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            if right == 0:
                return -1
            return right - 1 if nums[right - 1] == target else -1

        return [searchLeft(nums, target), searchRight(nums, target)]
