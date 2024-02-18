class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jumps = []
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                jumps.append((heights[i] - heights[i - 1], i))

        heap = []  # ladders
        heapify(heap)
        for (jump, idx) in jumps:
            heappush(heap, jump)
            ladders -= 1

            if ladders < 0:  # use bricks
                minjump = heappop(heap)
                bricks -= minjump

            if bricks < 0:
                return idx - 1

        return len(heights) - 1
