/*
 * I know the best answer code, but I wrote the below code with DP daringly.
 */
function maxProfit(prices: number[]): number {
  const numOfPrices = prices.length;
  const stateTable: number[][] = [
      // purchased price
      Array(numOfPrices + 1).fill(0),
      
      // profit
      Array(numOfPrices + 1).fill(0),
  ];
  stateTable[0][0] = 10000000;
  for (let i = 1; i < numOfPrices + 1; i++) {
      
      // Minimizes the cost
      stateTable[0][i] = Math.min(
          // The lowest price so far,
          stateTable[0][i - 1],
          
          // or we purchase at this time
          prices[i - 1],
      );
      
      // Maximizes the profit
      stateTable[1][i] = Math.max(
          
          // The maximum profit so far,
          stateTable[1][i - 1],
          
          // or sell the stock at this time
          prices[i - 1] - stateTable[0][i - 1],
      );
  }
  return stateTable[1][numOfPrices];
};
