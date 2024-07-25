class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(ls):
            if len(ls) == 1:
                return ls

            left = mergesort(ls[0:len(ls) // 2])
            right = mergesort(ls[len(ls) // 2:len(ls)])

            # merge
            new = []
            lidx, ridx = 0, 0
            while lidx + ridx < len(ls):
                if lidx < len(left) and (ridx == len(right) or left[lidx] < right[ridx]):
                    new.append(left[lidx])
                    lidx += 1
                else:
                    new.append(right[ridx])
                    ridx += 1

            return new

        return mergesort(nums)
