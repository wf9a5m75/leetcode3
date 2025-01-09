function lengthOfLongestSubstring(s: string): number {
  let l = 0;
  const appearsInWindow = new Set<string>();
  let result = 0;
  for (let r = 0; r < s.length; r++) {
      const char = s[r];
      if (!appearsInWindow.has(char)) {
          appearsInWindow.add(char);
          continue;
      }
      result = Math.max(result, r - l);
      while (appearsInWindow.has(char)) {
          appearsInWindow.delete(s[l]);
          l++;
      }
      appearsInWindow.add(char);
  }
  result = Math.max(result, s.length - l);
  return result;
};