from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    potential_matches = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in potential_matches:
            return [potential_matches[difference], i]
        potential_matches[num] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
