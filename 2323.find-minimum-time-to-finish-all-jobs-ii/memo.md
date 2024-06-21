# step1 : とりあえず思いつくコードで書いてみる

## 時間計算量：O(n log n)
- n は jobs.length
- ソートを2回 `O(2n log n)` と イテレーション `O(n)` なので、`O(2n log n) + O(n) = O(n log n)`

## 空間計算量：O(n)
- `sorted()` で新しい配列を生成しているので、`O(n)`

## メモ
- 別問題で、引数の配列は変更するのは好ましくない、というレビューをもらったので、新しい配列を生成した。
- fractionの使い方に少々戸惑ったが、ロジック自体はすぐにできた
- 浮動小数点計算を避けるために `Fraction`を使ったけど、`int(frac.numerator / frac.denominator) + 1` で使っていて、ここも避けるべきなのか？と疑問が残る
- (普通に `ceil` とかで良いのでは？)

```python
from fractions import Fraction
from typing import List

class Solution:
    
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        """
        Assign each work in order of workload and worker ability.
        """
        sorted_jobs = list(sorted(jobs))
        sorted_workers = list(sorted(workers))
        
        necessary_days = 1
        for job, worker in zip(sorted_jobs, sorted_workers):
            frac = Fraction(job, worker)
            
            days_to_complete = 0
            if frac.numerator < frac.denominator:
                days_to_complete = 1
            elif frac.denominator == 1:
                days_to_complete = frac.numerator
            else:
                days_to_complete = int(frac.numerator / frac.denominator) + 1
            
            necessary_days = max(necessary_days, days_to_complete)
        
        return necessary_days
        
```

ーーーーーーーーーーーーーーーーーーーーーー
# step2 : ceil を使ってやってみる

## 所要時間: 3分

## 時間計算量：O(n log n)
`step`と同じなので省略

## 空間計算量：O(n)
`step`と同じなので省略

## メモ：
- `ceil`のがコードとしてはシンプルで可読性が良い

```python
from typing import List

class Solution:
    
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # Assigning small jobs to small workers, large jobs to experts.
        sorted_jobs = sorted(jobs)
        sorted_workers = sorted(workers)

        # We need at least 1 day for any jobs.
        answer = 1
        for job, worker in zip(sorted_jobs, sorted_workers):
            necessary_days = ceil(job / worker)
            answer = max(answer, necessary_days)
        return answer
```
ーーーーーーーーーーーーーーーーーーーーーー
# step3 : いろいろ不便なTypeScriptでやってみる

## 所要時間: 5分

## 時間計算量：O(n log n)
`step`と同じなので省略

## 空間計算量：O(n)
`step`と同じなので省略

## メモ：
- `python`の直後だから、`sort()`で比較関数を付けなければならないのを忘れてた...

```typescript
function minimumTime(jobs: number[], workers: number[]): number {
    const sorted_jobs = numeric_sorted(jobs);
    const sorted_workers = numeric_sorted(workers);
    
    const job_nums = jobs.length;
    let answer = 1;
    for (let i = 0; i < job_nums; i++) {
        const job = sorted_jobs[i];
        const worker = sorted_workers[i];
        const necessary_days = Math.ceil(job / worker);
        answer = Math.max(answer, necessary_days);
    }
    return answer;
};
function numeric_sorted(arr: number[]): number[] {
    return Array.from(arr).sort((a, b) => a - b);
};
```