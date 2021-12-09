from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited = [False] * len(arr)
        visited[start] = True

        ans = False

        while queue:
            idx = queue.pop(0)

            if arr[idx] == 0:
                ans = True
                break

            left = idx - arr[idx]
            if left >= 0 and not visited[left]:
                queue.append(left)
                visited[left] = True

            right = idx + arr[idx]
            if right < len(arr) and not visited[right]:
                queue.append(right)
                visited[right] = True

        return ans
