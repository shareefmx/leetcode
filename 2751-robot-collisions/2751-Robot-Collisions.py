class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        order = sorted(range(len(positions)), key=lambda i: positions[i])
        stack = []

        for i in order:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top = stack[-1]
                    if healths[top] < healths[i]:
                        stack.pop()
                        healths[top] = 0
                        healths[i] -= 1
                    elif healths[top] == healths[i]:
                        stack.pop()
                        healths[top] = 0
                        healths[i] = 0
                    else:
                        healths[top] -= 1
                        healths[i] = 0

        return [h for h in healths if h > 0]