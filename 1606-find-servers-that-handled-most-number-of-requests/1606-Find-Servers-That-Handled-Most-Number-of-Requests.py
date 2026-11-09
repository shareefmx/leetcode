import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

       
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

       
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(pos, value):
            pos += size
            tree[pos] = value

            pos //= 2

            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find(node, left, right, start):

            if right < start or tree[node] == 0:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2

            result = find(2 * node, left, mid, start)

            if result != -1:
                return result

            return find(2 * node + 1, mid + 1, right, start)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            while busy and busy[0][0] <= arrival[i]:

                end_time, server = heapq.heappop(busy)

                update(server, 1)

            start = i % k

            server = find(1, 0, size - 1, start)

            if server == -1:
                server = find(1, 0, size - 1, 0)

            if server == -1 or server >= k:
                continue
            count[server] += 1

            update(server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]