function maxProfit(prices: number[]): number {
  const dp = new Array(prices.length + 1).fill(0);
  let purchase = Number.POSITIVE_INFINITY;
  for (let i = 0; i < prices.length; i++) {
      if (purchase < prices[i]) {
          dp[i + 1] = dp[i] + prices[i] - purchase;
      } else {
          dp[i + 1] = Math.max(dp[i + 1], dp[i]);
      }
      purchase = prices[i];
  }
  return dp[prices.length];
};