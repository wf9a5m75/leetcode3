function mergeAlternately(word1: string, word2: string): string {
  let buffer: string[] = [];
  let i = 0;
  let j = 0;
  while (i < word1.length || j < word2.length) {
      if (i < word1.length) {
          buffer.push(word1[i]);
          i++;
      }
      if (j < word2.length) {
          buffer.push(word2[j]);
          j++;
      }
  }
  return buffer.join('');
};