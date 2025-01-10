function maxProfit(prices: number[]): number {
  const dp: number[] = Array(prices.length + 1).fill(1000000);
  let result = 0;
  for (let i = 0; i < prices.length; i++) {
      const price = prices[i];

      // Chooses a smaller price
      dp[i + 1] = Math.min(
          // If we buy a stack at i, or
          price,
          // we use the previous stack cost
          dp[i],
      );

      // Maximizes the profit
      result = Math.max(result, price - dp[i]);
  }
  return result;
};