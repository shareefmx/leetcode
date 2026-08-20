class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(n):
            if n < 100:
                return 0

            digits = list(map(int, str(n)))
            length = len(digits)

            from functools import lru_cache

            @lru_cache(None)
            def dp(pos, prev2, prev, tight, started):
                if pos == length:
                    return (0, 1)

                limit = digits[pos] if tight else 9
                total_waviness = 0
                total_count = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        w, cnt = dp(pos + 1, -1, -1, ntight, False)
                    elif not started:
                        w, cnt = dp(pos + 1, -1, d, ntight, True)
                    else:
                        w, cnt = dp(pos + 1, prev, d, ntight, True)

                    extra = 0
                    if started and prev2 != -1:
                        if prev > prev2 and prev > d:
                            extra = 1
                        elif prev < prev2 and prev < d:
                            extra = 1

                    total_waviness += w + extra * cnt
                    total_count += cnt

                return total_waviness, total_count

            return dp(0, -1, -1, True, False)[0]

        return calc(num2) - calc(num1 - 1)