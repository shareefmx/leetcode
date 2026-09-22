class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [(0, [0] * k) for _ in range(4 * n)]

        def merge(a, b):
            ap, ac = a
            bp, bc = b
            p = ap * bp % k
            c = ac[:]

            for r in range(k):
                c[ap * r % k] += bc[r]

            return p, c

        def build(i, l, r):
            if l == r:
                x = nums[l] % k
                c = [0] * k
                c[x] = 1
                tree[i] = (x, c)
                return

            m = (l + r) // 2
            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def update(i, l, r, pos, val):
            if l == r:
                x = val % k
                c = [0] * k
                c[x] = 1
                tree[i] = (x, c)
                return

            m = (l + r) // 2

            if pos <= m:
                update(i * 2, l, m, pos, val)
            else:
                update(i * 2 + 1, m + 1, r, pos, val)

            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def query(i, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[i]

            m = (l + r) // 2

            if qr <= m:
                return query(i * 2, l, m, ql, qr)

            if ql > m:
                return query(i * 2 + 1, m + 1, r, ql, qr)

            return merge(
                query(i * 2, l, m, ql, qr),
                query(i * 2 + 1, m + 1, r, ql, qr)
            )

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            _, count = query(1, 0, n - 1, start, n - 1)
            ans.append(count[x])

        return ans