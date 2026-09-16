from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1 = [-9999999] + nums1 + [9999999]
        nums2 = [-9999999] + nums2 + [9999999]

        low = 0
        high = len(nums1)

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (len(nums1) + len(nums2) + 1) // 2 - partition_x

            max_left_x = nums1[max(0, partition_x - 1)]
            min_right_x = nums1[min(len(nums1) - 1, partition_x)]
            max_left_y = nums2[max(0, partition_y - 1)]
            min_right_y = nums2[min(len(nums2) - 1, partition_y)]

            if max_left_x <= min_right_y and min_right_x >= max_left_y:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)

            if min_right_x < max_left_y:
                low = partition_x + 1
            else:
                high = partition_x - 1

        return 0.0
