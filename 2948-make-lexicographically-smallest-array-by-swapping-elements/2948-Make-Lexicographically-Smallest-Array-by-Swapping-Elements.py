class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        arr = sorted((value, i) for i, value in enumerate(nums))
        ans = nums[:]

        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = sorted(arr[i][1] for i in range(start, end + 1))

            for k, idx in enumerate(indices):
                ans[idx] = arr[start + k][0]

            start = end + 1

        return ans