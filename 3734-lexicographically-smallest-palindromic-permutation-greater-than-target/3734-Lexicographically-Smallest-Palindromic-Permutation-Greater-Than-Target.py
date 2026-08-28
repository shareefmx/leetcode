class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        freq = Counter(s)

        odd = [c for c in freq if freq[c] % 2]
        if len(odd) > 1:
            return ""

        half = [0] * 26
        for i in range(26):
            half[i] = freq[chr(97 + i)] // 2

        center = odd[0] if n % 2 else ""

        def build(left):
            return left + center + left[::-1] if n % 2 else left + left[::-1]

        cnt = half[:]
        left = []

        for ch in target[:n // 2]:
            i = ord(ch) - 97
            if cnt[i] == 0:
                break
            cnt[i] -= 1
            left.append(ch)
        else:
            ans = build("".join(left))
            if ans > target:
                return ans

        for i in range(n // 2 - 1, -1, -1):
            cnt = half[:]

            for ch in target[:i]:
                j = ord(ch) - 97
                if cnt[j] == 0:
                    break
                cnt[j] -= 1
            else:
                for j in range(ord(target[i]) - 96, 26):
                    if cnt[j] == 0:
                        continue

                    cnt[j] -= 1
                    suffix = []

                    for k in range(26):
                        suffix.extend([chr(97 + k)] * cnt[k])

                    left = target[:i] + chr(97 + j) + "".join(suffix)
                    return build(left)

        return ""