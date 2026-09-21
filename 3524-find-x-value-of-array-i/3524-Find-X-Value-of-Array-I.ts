function resultArray(nums: number[], k: number): number[] {
    const ans = new Array(k).fill(0);

    let dp = new Array(k).fill(0);

    for (const num of nums) {
        const x = num % k;

        const next = new Array(k).fill(0);
        next[x]++;
        for (let r = 0; r < k; r++) {
            if (dp[r] > 0) {
                const newRemainder = (r * x) % k;
                next[newRemainder] += dp[r];
            }
        }

        dp = next;

        for (let r = 0; r < k; r++) {
            ans[r] += dp[r];
        }
    }

    return ans;
}