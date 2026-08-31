class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        pos = 1
        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next
            pos += 1

            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):

                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = nxt

        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]