/**
 * N ... prices.length
 * TC: O(N) ... The remain takes 3 patterns (0, 1, and 2), also holding takes 2 patterns (true and false), but we can ignore them.
 * SC: O(N)
 */
function maxProfit(prices: number[]): number {
  const cache = new Map<string, number>();
  
  const backtrack = (idx: number, remain: number, holding: boolean): number => {
      if (idx === prices.length || remain === 0) {
          return 0;
      }
      const key = `${idx}_${remain}_${holding}`;
      if (cache.has(key)) {
          return cache.get(key)!;
      }
      
      const doNothing = backtrack(idx + 1, remain, holding);
      let doSomething = 0;
      
      if (holding) {
          // Sell the holding stock
          doSomething = prices[idx] + backtrack(idx + 1, remain - 1, false);
      } else {
          // Buy a stock
          // Since we don't sell the stock yet, keep the remaining count.
          doSomething = -prices[idx] + backtrack(idx + 1, remain, true);
      }
      const result = Math.max(doNothing, doSomething);
      cache.set(key, result);
      
      return result;
  };
  
  return backtrack(0, 2, false);
};