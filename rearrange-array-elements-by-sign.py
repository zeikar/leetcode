class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_idx, neg_idx = 0, 0
        res = [0] * len(nums)
        for num in nums:
            if num < 0:
                res[neg_idx * 2 + 1] = num
                neg_idx += 1
            else:
                res[pos_idx * 2] = num
                pos_idx += 1
        return res
