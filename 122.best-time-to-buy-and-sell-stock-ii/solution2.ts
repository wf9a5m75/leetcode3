function maxProfit(prices: number[]): number {
  const dp = new Array(prices.length + 1).fill(0);
  let purchase = Number.POSITIVE_INFINITY;
  for (let i = 0; i < prices.length; i++) {
      dp[i + 1] = Math.max(
          // case 1: Do nothing
          dp[i + 1],
          // case 2: Do nothing
          dp[i],
          // case 3: Sell the stock
          dp[i] + prices[i] - purchase,
      )
      // purchase the stock
      purchase = prices[i];
  }
  return dp[prices.length];
};