import re
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        arr = re.split(r"[()]", s)
        knowledge = dict(knowledge)
        for i in range(len(arr)):
            if i % 2 == 1:
                arr[i] = knowledge.get(arr[i], "?")
        return "".join(arr)