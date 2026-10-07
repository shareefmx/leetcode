class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        res = []
        path = []
        n = len(s)

        def dfs(i, left_rem, right_rem, balance):
            if i == n:
                if left_rem == 0 and right_rem == 0 and balance == 0:
                    res.append("".join(path))
                return

            ch = s[i]

            if ch == '(':
                if left_rem > 0 and (i == 0 or s[i - 1] != '('):
                    dfs(i + 1, left_rem - 1, right_rem, balance)
                path.append(ch)
                dfs(i + 1, left_rem, right_rem, balance + 1)
                path.pop()

            elif ch == ')':
                if right_rem > 0 and (i == 0 or s[i - 1] != ')'):
                    dfs(i + 1, left_rem, right_rem - 1, balance)
                if balance > 0:
                    path.append(ch)
                    dfs(i + 1, left_rem, right_rem, balance - 1)
                    path.pop()

            else:
                path.append(ch)
                dfs(i + 1, left_rem, right_rem, balance)
                path.pop()

        dfs(0, left_rem, right_rem, 0)
        return res