class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)

        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)
        prefix = [0] * (4 * n)
        suffix = [0] * (4 * n)
        best = [0] * (4 * n)

        def build(node, l, r):
            if l == r:
                left_char[node] = right_char[node] = s[l]
                prefix[node] = suffix[node] = best[node] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            merge(node, node * 2, node * 2 + 1, mid - l + 1, r - mid)

        def merge(node, left, right, left_len, right_len):
            left_char[node] = left_char[left]
            right_char[node] = right_char[right]

            prefix[node] = prefix[left]
            suffix[node] = suffix[right]

            if prefix[left] == left_len and right_char[left] == left_char[right]:
                prefix[node] = left_len + prefix[right]

            if suffix[right] == right_len and right_char[left] == right_char[right]:
                suffix[node] = right_len + suffix[left]

            best[node] = max(best[left], best[right])

            if right_char[left] == left_char[right]:
                best[node] = max(
                    best[node],
                    suffix[left] + prefix[right]
                )

        def update(node, l, r, idx, char):
            if l == r:
                left_char[node] = right_char[node] = char
                prefix[node] = suffix[node] = best[node] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            merge(
                node,
                node * 2,
                node * 2 + 1,
                mid - l + 1,
                r - mid
            )

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(best[1])

        return ans