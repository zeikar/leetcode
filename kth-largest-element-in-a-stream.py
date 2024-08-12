class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()

        self.k = k
        self.largeHeap = nums[-k:]
        heapq.heapify(self.largeHeap)

    def add(self, val: int) -> int:
        if len(self.largeHeap) < self.k:
            heapq.heappush(self.largeHeap, val)
        elif val > self.largeHeap[0]:
            heapq.heappop(self.largeHeap)
            heapq.heappush(self.largeHeap, val)

        return self.largeHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
