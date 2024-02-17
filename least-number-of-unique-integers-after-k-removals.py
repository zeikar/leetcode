class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = defaultdict(int)
        for num in arr:
            cnt[num] += 1

        removed = 0
        for (_, v) in sorted(cnt.items(), key=lambda item: item[1]):
            if k == 0:
                return len(cnt) - removed
            if k < v:
                return len(cnt) - removed
            k -= v
            removed += 1
        return 0
