class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        res = -1
        perimeter = 0
        for num in nums:
            if perimeter > num:
                res = perimeter + num
            perimeter += num

        return res
