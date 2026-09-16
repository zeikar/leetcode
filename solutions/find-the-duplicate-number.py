from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = 0
        tortoise = 0
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break

        tortoise = 0
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]

        return hare
