function coinChange(coins: number[], amount: number): number {
    const INFINITY = Number.POSITIVE_INFINITY;
    const dp = new Array(amount + 1).fill(INFINITY);
    dp[0] = 0;

    for (let i = 0; i < amount; i++) {
        for (const coin of coins) {
            if (i + coin > amount) {
                continue;
            }

            dp[i + coin] = Math.min(dp[i + coin], dp[i] + 1);
        }
    }
    if (dp[amount] === INFINITY) {
        return -1;
    }
    return dp[amount];
};