function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
      return false;
  }
  const count = new Map<string, number>();
  for (const char of s) {
      count.set(char, (count.get(char) || 0) + 1);
  }
  for (const char of t) {
      const prev = count.get(char) || 0;
      if (prev === 0) {
          return false;
      }
      count.set(char, prev - 1);
  }
  for (const cnt of count.values()) {
      if (cnt !== 0) {
          return false;
      }
  }
  return true;
};