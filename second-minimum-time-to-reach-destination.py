from sortedcontainers import SortedList


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        pq = [(0, 1)]
        graph = defaultdict(list)
        visitcnt = defaultdict(int)
        distance = [[float('inf')] * 2 for _ in range(n + 1)]
        distance[1][0] = 0

        # time의 짝수 배수와 홀수 배수 사이면 바로 출발
        # 홀수 배수와 짝수 배수 사이면 짝수 배수까지 대기
        def caltime(dist):
            if (dist // change) % 2 == 0:
                return dist
            return (dist // change) * change + change

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        while len(pq) > 0:
            current = heapq.heappop(pq)
            [d, c] = current

            visitcnt[c] += 1
            if visitcnt[c] >= 2 and c == n:
                return d

            for next in graph[c]:
                if visitcnt[next] >= 2:
                    continue

                cal = caltime(d) + time
                if distance[next][0] > cal:
                    distance[next][1] = distance[next][0]
                    distance[next][0] = cal
                    heapq.heappush(pq, (cal, next))
                elif distance[next][1] > cal and distance[next][0] < cal:
                    distance[next][1] = cal
                    heapq.heappush(pq, (cal, next))

        return 0
