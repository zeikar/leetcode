class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        lines = []
        for building in buildings:
            lines.append([building[0], -building[2], building[1]])
            lines.append([building[1], building[2], 0])
        lines.sort()
        print(lines)

        ans = []
        heights = [[0, inf]]
        for line in lines:
            [x, h, r] = line

            if r == 0:
                if -heights[0][0] > h:
                    continue

                while -heights[0][0] <= h and heights[0][1] <= x:
                    heapq.heappop(heights)

                if ans[-1][1] != -heights[0][0]:
                    ans.append([x, -heights[0][0]])
            else:
                h *= -1

                if -heights[0][0] >= h:
                    heapq.heappush(heights, [-h, r])
                    continue

                heapq.heappush(heights, [-h, r])
                ans.append([x, h])

        return ans
