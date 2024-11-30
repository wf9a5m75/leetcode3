function isPalindrome(s: string): boolean {
  let left = 0;
  let right = s.length - 1;
  s = s.toLowerCase();
  const alphabets = new Set('abcdefghijklmnopqrstuvwxyz0123456789'.split(''));
  while (left <= right) {
      while (left < s.length && !alphabets.has(s[left])) { 
          left++;
      }
      while (0 <= right && !alphabets.has(s[right])) { 
          right--;
      }
      if (s[left] !== s[right]) {
          return false;
      }
      left++;
      right--;
  }
  return true;
};
