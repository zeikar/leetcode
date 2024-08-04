class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @cache
        def swap(idx, swapped):
            if idx == n:
                return 0

            ret = 987654321
            if swapped:
                if nums1[idx - 1] < nums2[idx] and nums2[idx - 1] < nums1[idx]:
                    ret = min(ret, swap(idx + 1, False))

                if nums1[idx - 1] < nums1[idx] and nums2[idx - 1] < nums2[idx]:
                    ret = min(ret, swap(idx + 1, True) + 1)

            else:
                if nums1[idx - 1] < nums1[idx] and nums2[idx - 1] < nums2[idx]:
                    ret = min(ret, swap(idx + 1, False))

                if nums1[idx - 1] < nums2[idx] and nums2[idx - 1] < nums1[idx]:
                    ret = min(ret, swap(idx + 1, True) + 1)

            return ret

        return min(swap(1, False), swap(1, True) + 1)
