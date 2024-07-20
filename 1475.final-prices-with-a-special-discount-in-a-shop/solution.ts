function finalPrices(prices: number[]): number[] {
  const answer: number[] = Array.from(prices);
  
  const pricesJ: number[] = [];
  for (let i = prices.length - 1; i >= 0; i--) {
      const priceI = prices[i];
      
      while (pricesJ.length > 0 && pricesJ[pricesJ.length - 1] > priceI) {
          pricesJ.pop();
      }
      
      if (pricesJ.length === 0) {
          answer[i] = priceI;
      } else {
          answer[i] = priceI - pricesJ[pricesJ.length - 1];
      }
      
      pricesJ.push(priceI);
  }
  return answer;
};