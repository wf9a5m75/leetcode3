function groupAnagrams(strs: string[]): string[][] {
  const memo = new Map<number, string[]>();
  
  strs.forEach(word => {
      const key = primeHash(word);
      const groups = memo.get(key) || [];
      groups.push(word);
      memo.set(key, groups);
  });

  return Array.from(memo.values());
};

const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101];
const charCode_a = "a".charCodeAt(0);

function primeHash(str: string): number {
  return Array.from(str).reduce((prev, curr) => {
      return prev * primes[curr.charCodeAt(0) - charCode_a];
  }, 1);
}