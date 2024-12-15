function longestCommonSubsequence(text1: string, text2: string): number {
  const text1Len = text1.length;
  const text2Len = text2.length;
  
  // Initialize the DP matrix
  const matching: number[][] = Array(text1Len + 1);
  for (let i = 0; i < text1Len + 1; i++) {
      matching[i] = Array(text2Len + 1).fill(0);
  }
  
  for (let i = 1; i <= text1Len; i++) {
      for (let j = 1; j <= text2Len; j++) {
          matching[i][j] = Math.max(
              // text2[j]から始めた場合
              matching[i][j - 1],
              // 前の文字から引き継いだ場合
              matching[i - 1][j],
              // 前の文字から連続した場合
              matching[i - 1][j - 1] + (text1[i - 1] === text2[j - 1] ? 1 : 0));
      }
  }
  
  // for (let i = 0; i <= text1Len; i++) {
  //     console.log(JSON.stringify(matching[i]));
  // }
  
  return matching[text1Len][text2Len];
};
