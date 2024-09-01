class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        prob = [0] * n
        prob[start_node] = 1
        pq = [(-1, start_node)]
        while len(pq) > 0:
            current = heapq.heappop(pq)
            (p, c) = current
            p *= -1
            if c == end_node:
                return p

            for g in graph[c]:
                next = g[0]
                np = p * g[1]

                if prob[next] < np:
                    heapq.heappush(pq, (-np, next))
                    prob[next] = np

        return 0.0