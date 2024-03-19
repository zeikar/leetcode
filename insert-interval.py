class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resleft, resright = [], []
        [newLeft, newRight] = newInterval
        overlapLeft, overlapRight = newLeft, newRight

        for interval in intervals:
            [left, right] = interval

            if right < newLeft:
                resleft.append(interval)
            elif left > newRight:
                resright.append(interval)
            else:
                overlapLeft = min(overlapLeft, left)
                overlapRight = max(overlapRight, right)

        resleft.append([overlapLeft, overlapRight])
        resleft.extend(resright)
        return resleft
