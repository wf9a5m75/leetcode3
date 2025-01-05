function totalFruit(fruits: number[]): number {
  let result = 0;

  // フルーツが現れた最初のインデックスと、同じ種類のフルーツが最後に現れたインデックスを記録する
  // バスケット1が常に先に現れたフルーツを格納する
  let basket1: number[] = [0, 0];
  let basket2: number[] = [-1, -1];

  for (let i = 0; i < fruits.length; i++) {
      const kind = fruits[i];

      // バスケット1のフルーツと同じなら、現在位置との距離がフルーツの数
      if (fruits[basket1[0]] === kind) {
          basket1[1] = i;
          result = Math.max(result, i - basket1[0] + 1);
          continue;
      }
      // バスケット2が空なら、新しいフルーツを入れる
      if (basket2[0] === -1) {
          basket2[0] = i;
          basket2[1] = i;
          result = Math.max(result, i - basket1[0] + 1);
          continue;
      }
      // バスケット2のフルーツと同じなら、現在位置との距離がフルーツの数
      if (fruits[basket2[0]] === kind) {
          basket2[1] = i;
          result = Math.max(result, i - basket1[0] + 1);
          continue;
      }

      // 新しいフルーツの種類になった場合
      // バスケット1,2のうち最後に現れたフルーツのインデックスが
      // 前のフルーツの次(+1)が、現在のインデックス-1まで続いている
      //
      // e.g. [1, 2, 2, 1, 1, 3, 2, 3]
      // i = 5 のとき、
      // basket1 = [0, 4], basket2 = [1, 2] になっている.
      // basket2[1] = 2なので、その次のインデックスから、i - 1までが同じ種類のフルーツになる
      if (basket1[1] < basket2[1]) {
          basket1[0] = basket1[1] + 1;
          basket1[1] = basket2[1];
      } else {
          basket1[0] = basket2[1] + 1;
          basket1[1] = basket1[1];
      }
      basket2[0] = i;
      basket2[1] = i;
  }

  return result;
};