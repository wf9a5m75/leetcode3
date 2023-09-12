function reverseWords(s: string): string {
  s = s.trim().replace(/\s+/g, ' ');
  const words = s.split(' ')
  return words.reverse().join(' ');
};