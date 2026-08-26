class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            if ones == k:

                while s[left] == '0':
                    left += 1

                candidate = s[left:right + 1]

                if (not best or
                    len(candidate) < len(best) or
                    (len(candidate) == len(best) and candidate < best)):
                    best = candidate

                ones -= 1
                left += 1

        return best