class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda item: item[0])
        rooms = [0] * n
        cnt = defaultdict(int)

        for meeting in meetings:
            min_room = 0
            for i in range(n):
                if rooms[i] <= meeting[0]:
                    min_room = i
                    break
                if rooms[min_room] > rooms[i]:
                    min_room = i

            if rooms[min_room] <= meeting[0]:
                rooms[min_room] = meeting[1]
            else:
                rooms[min_room] += (meeting[1] - meeting[0])
            cnt[min_room] += 1

        cnt = sorted(cnt.items(), key=lambda item: item[1], reverse=True)
        return cnt[0][0]
