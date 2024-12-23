function maxProfit(prices: number[]): number {
  const profitAndCostTable: number[][][] = [
      [[0, 0], [0, 0], [0, 0]],
      [[0, 0], [0, 0], [0, 0]],
  ];
  
  
  let currentIdx = 0;
  let prevIdx = 1;
  for (let i = prices.length - 1; i >= 0; i--) {
      for (let remain = 2; remain >= 1; remain--) {
          for (let holding = 0; holding <= 1; holding++) {
              const doNothing = profitAndCostTable[prevIdx][remain][holding];
              let doSomething = 0;
              
              if (holding === 0) {
                  // Buy a stock
                  doSomething = profitAndCostTable[prevIdx][remain][1] - prices[i];
                  
              } else {
                  // Sell the holding stock
                  doSomething = profitAndCostTable[prevIdx][remain - 1][0] + prices[i];
              }
              profitAndCostTable[currentIdx][remain][holding] = Math.max(doNothing, doSomething);
          }
      }
      prevIdx = currentIdx;
      currentIdx = (currentIdx + 1) % 2;
  }
  
  return Math.max(profitAndCostTable[prevIdx][0][0], profitAndCostTable[prevIdx][1][0], profitAndCostTable[prevIdx][2][0]);
};
