import heapq

def assignTasks(servers, tasks):
    free = [(w, i) for i, w in enumerate(servers)]
    heapq.heapify(free)
    busy = []                     
    ans = []
    t = 0

    for j, dur in enumerate(tasks):
        t = max(t, j)             
        if not free:              
            t = max(t, busy[0][0])
        while busy and busy[0][0] <= t:
            _, w, i = heapq.heappop(busy)
            heapq.heappush(free, (w, i))
        w, i = heapq.heappop(free)
        ans.append(i)
        heapq.heappush(busy, (t + dur, w, i))

    return ans