function pancakeSort(arr: number[]): number[] {
    
    const flip = (k: number) => {
        let left = 0;
        let right = k;
        let tmp = 0;
        while (left < right) {
            tmp = arr[left];
            arr[left] = arr[right]
            arr[right] = tmp;
            left++;
            right--;
        }
    }
    
    // バブルソートを用いる
    // target(処理されていない一番大きな数字)を、flip(k)で一番左に持ってくる
    // 本来あるべき位置に、もう一度flip(taregt)を行って移動させる
    // target を1つ減らす
    const results: number[] = [];
    for (let target = arr.length; target > 1; target--) {
        let k = arr.indexOf(target);
        while (k !== target - 1) {
            if (k > 0) {
                results.push(k + 1);
                flip(k);
            } else {
                results.push(target);
                flip(target - 1);
            }
            k = arr.indexOf(target);
        }
    }
    
    return results;
};
