# step1: 思い付いたコードで書く

## 所要時間
- 7分程度

## 時間計算量：O(log n)
- n は arr.length
- arr[mid] == mid で見つかった場合、さらに左側の範囲であるかもしれないので、再帰呼出しで二分探索を行う
- arr[mid] = mid が 最大N個 (arr = [0,1,2,3...]) あるとして、見つかっても探索を続けているだけなので、普通の二分探索と同じため、`O(log n)` となる。

## 空間計算量: O(1)
特にメモリ空間は確保していない

## メモ

後から考えると、再帰呼出しする必要性はなくて、単純に二分探索を継続すれば良いだけなので、もう少しコードがシンプルになる

```python
from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        return self.binarySearchWithBounds(arr, 0, len(arr) - 1)
        
    def binarySearchWithBounds(self, arr: List[int], start: int, end: int) -> int:
        if (start > end):
            return -1
        L = start
        R = end
        while L <= R:
            mid = (L + R) >> 1
            if arr[mid] == mid:
                left_side = self.binarySearchWithBounds(arr, L, mid - 1)
                if left_side > -1:
                    return left_side
                return mid
            
            if arr[mid] < mid:
                L = mid + 1
            else:
                R = mid - 1
        return -1
```

--------------------------------------------------------------------------------
# step2: 変形してみる1

## 所要時間
- 3分

## 時間計算量：O(log n)
- step1と同じなので、省略
## 空間計算量: O(1)
- step1と同じなので、省略

## メモ
- 再帰呼出しをしないで実装。シンプル。
- `(L + R) >> 1` は、`(L + R) // 2` と基本的には同義。
- ただし`//` は、丸め誤差があったはずで、何度か痛い目を過去に見ているので、`int((L + R) / 2)`を使うようにしている。
- `x >> 1`は、使えるときだけ使う。（ビットシフトの使用は好み）

```python
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        L = 0
        R = len(arr) - 1
        ans = -1
        while (L <= R):
            mid = (L + R) >> 1
            if arr[mid] == mid:
                # update the answer
                ans = mid
                # We only need to check in the left side from the mid
                R = mid - 1
                continue
            
            if arr[mid] > mid:
                R = mid - 1
            else:
                L = mid + 1
        return ans
```

--------------------------------------------------------------------------------
# step3: 変形してみる2

## 所要時間
- 3分

## 時間計算量：O(log n)
- step1と同じなので、省略
## 空間計算量: O(1)
- step1と同じなので、省略

## メモ
- 可読性を考慮して、書き直してみた。

```python
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        answer = -1
        while left <= right:
            middle = int((left + right) / 2)
            
            if arr[middle] < middle:
                left = middle + 1
            elif arr[middle] == middle:
                answer = middle
                right = middle - 1
            else:
                right = middle - 1
        return answer
```
