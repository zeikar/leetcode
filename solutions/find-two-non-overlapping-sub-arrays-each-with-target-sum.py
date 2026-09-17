class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        arr.append(987654321)
        minLen = [987654321 for _ in range(n)]

        l, r = 0, 0
        s = 0
        while l <= r:
            if l == n:
                break
            
            if s < target:
                if r > 1:
                    minLen[r-1] = min(minLen[r-1], minLen[r-2])
                s += arr[r]
                r += 1
            elif s == target:
                if r > 1:
                    minLen[r-1] = min(minLen[r-1], minLen[r-2])
                minLen[r-1] = min(minLen[r-1], r - l)
                s += arr[r]
                r += 1
            else:
                s -= arr[l]
                l += 1
        
        ans = 987654321
        l, r = 0, 0
        s = 0
        while l <= r:
            if l == n:
                break
            
            if s < target:
                s += arr[r]
                r += 1
            elif s == target:
                if l > 0:
                    ans = min(ans, minLen[l-1] + r - l)
                s += arr[r]
                r += 1
            else:
                s -= arr[l]
                l += 1

        return ans if ans != 987654321 else -1
