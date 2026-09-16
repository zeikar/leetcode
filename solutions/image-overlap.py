from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        res = 0

        for r in range(-n, n):
            for c in range(-n, n):
                cnt = 0
                for x in range(max(-r, 0), min(n-r, n)):
                    for y in range(max(-c, 0), min(n-c, n)):
                        cnt += 1 if img1[x+r][y+c] == img2[x][y] and img2[x][y] == 1 else 0

                res = max(res, cnt)

        return res
