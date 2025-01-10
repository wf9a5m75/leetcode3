function rob(nums: number[]): number {

  const moneyState: number[] = new Array(nums.length + 2).fill(0);

  for (let i = 0; i < nums.length; i++) {
      // robbering
      moneyState[i + 2] = moneyState[i] + nums[i];

      // do nothing
      moneyState[i + 1] = Math.max(moneyState[i + 1], moneyState[i]);
  }

  return Math.max(moneyState[nums.length], moneyState[nums.length + 1]);
}