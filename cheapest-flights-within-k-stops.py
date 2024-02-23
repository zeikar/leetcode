class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graphs = [[] for i in range(n)]
        for f in flights:
            graphs[f[0]].append((f[1], f[2]))
        pq = [(0, src, k + 1)]
        stops = [0] * n

        while pq:
            cost, current, stop = heappop(pq)

            if current == dst:
                return cost

            if stops[current] >= stop:
                continue
            stops[current] = stop

            for next, price in graphs[current]:
                heappush(pq, (cost + price, next, stop - 1))

        return -1
