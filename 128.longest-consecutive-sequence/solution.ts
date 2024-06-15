function longestConsecutive(nums: number[]): number {
  const belongs = new Map<number, number>();
  const parents = new Map<number, number>();
  const counts = new Map<number, number>();
  
  let result = 0;
  let groupCnt = 0;
  nums.forEach(num => {
      const deltas = [-1, 0, 1];
      
      // console.log(`----[${num}]-------`)
      // console.log("belongs:", belongs)
      // console.log("parents:", parents)
      // Find groups for num including +/- 1
      const roots = deltas.map(delta => {
          const key = num + delta;
          if (!belongs.has(key)) {
              return -1;
          }
          
          const parent = belongs.get(key)!;
          return findRoot(parents, parent);
      });
      
      // Since the num and num +/- 1 do not appear yet,
      // create a new group
      const groups = roots.filter(x => x !== -1);
      if (groups.length === 0) {
          const newRoot = groupCnt;
          belongs.set(num, newRoot);
          parents.set(newRoot, newRoot);
          counts.set(newRoot, 1);
          
          groupCnt++;
          result = Math.max(result, 1);
          // console.log(`(new)${num} -> group:${newRoot}, total = 1`);
          return;
      }
      
      // Merge groups
      const newRoot = groupCnt;
      
      groupCnt++;
      const total = roots.reduce((accumerate, root) => {
          if (root === -1) {
              return accumerate;
          }
          
          // Update the parent index
          parents.set(root, newRoot);
          const cnt = counts.get(root)!;
          counts.set(root, 0);
          
          // Merge counts
          return accumerate + cnt;
      }, 0) + (roots[1] === -1 ? 1 : 0);
      
      belongs.set(num, newRoot);
      parents.set(newRoot, newRoot);
      counts.set(newRoot, total);
      // console.log(`  ${num} -> root = ${newRoot}, total = ${total}`);
      
      result = Math.max(result, total);
  });
  
  return result;
};

function findRoot(parents: Map<number, number>, curr: number): number {
  if (!parents.has(curr)) {
      return -1;
  }
  
  let parent = curr;
  while (parents.get(parent) !== parent) {
      parent = parents.get(parent)!;
  }
  parents.set(curr, parent);
  return parent;
};