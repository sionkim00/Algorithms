                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
            while busy and busy[0][0] <= start:
                recentEnd, room = heapq.heappop(busy)

        for start, end in meetings:

        meetings.sort()
        ans = [0] * n
        available = [i for i in range(n)]
                heapq.heappush(busy, [end, room])
            else:
                time, room = heapq.heappop(busy)
2
