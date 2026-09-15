class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            for j in range(i + k, n + 1):
                sub = s[i:j]

                if sub == sub[::-1]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return dp[0]