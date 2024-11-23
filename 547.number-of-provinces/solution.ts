function findCircleNum(isConnected: number[][]): number {
  const numOfCities = isConnected.length;
  const belongs = new Array<number>(numOfCities).fill(0);
  const groups: { [key: number]: number } = {};
  
  const findRoot = (root: number): number => {
      if (groups[root] === root) {
          return root;
      }
      groups[root] = findRoot(groups[root]);
      return groups[root];
  };
  
  for (let i = 0; i < numOfCities; i++) {
      // 自分自身が所属するグループを生成する
      groups[i] = i;
      // 自分自身が所属するグループを設定する
      belongs[i] = i;
  }
  
  let numOfGroups = numOfCities;
  for (let me = 0; me < numOfCities; me++) {
      for (let you = me + 1; you < numOfCities; you++) {
          // 2つの市が繋がっていなければスキップ
          if (isConnected[me][you] === 0) {
              continue;
          }
          
          // 自分自身と相手が所属するグループを取得
          const myRoot = findRoot(belongs[me]);
          const yourRoot = findRoot(belongs[you]);
          
          // 同じならスキップ
          if (myRoot === yourRoot) {
              continue;
          }
          
          // 違う場合は新しいグループを作成して、両方ともそちらに所属させる
          const newGroupId = ++numOfGroups;
          groups[newGroupId] = newGroupId;
          groups[myRoot] = newGroupId;
          groups[yourRoot] = newGroupId;
      }
  }
  
  
  let provinces = 0;
  for (let i = 0; i <= numOfGroups; i++) {
      if (groups[i] === i) {
          provinces++;
      }
  }
  return provinces;
};
