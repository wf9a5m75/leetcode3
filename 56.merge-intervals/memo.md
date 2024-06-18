# step1: 思いついたコードで書く

## 時間
7分

## 時間計算量: O(n log n)
- 最初にintervals を開始時間でソートしている。問題文にはソートされているとは書いていないので、ソートする必要性がある。O(n log n)
- 続くfor文では、全ての interval を見る必要があるので、O(n) の計算量がかかる。
- O(n log n + n) なので、全体としては O(n log n) がかかる。 

## 空間計算量: O(n) 
- 重なるintervalがない場合、results には intervals と同じ値が入るため。

```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        results = []
        start_time = intervals[0][0]
        end_time = intervals[0][1]
        for interval in intervals:
            if interval[0] <= end_time:
                end_time = max(end_time, interval[1])
                continue
                
            results.append([start_time, end_time])
            start_time = interval[0]
            end_time = interval[1]
        
        results.append([start_time, end_time])
        return results
        
```

----------------------------------------------------

# step2: step1を書き直してみる

## 時間
5分

## 時間計算量: O(n log n)
step1と同じなので省略

## 空間計算量: O(n) 
step1と同じなので省略

## 変更点
- `results` の最後の要素を使って、ある地点での interval の終了時間と、ループ地点での interval の開始時間について比較している。コードとしてはシンプルになるが、`results[-1][1]` という書き方は、可読性が悪いので、好みではない。
- pythonのsort() 関数は、評価対象 (ここではintervals[i]) が複数要素の場合、とくにキーを指定しなくても同一なら、インデックス順に intervals[i][0,1,2...]  と勝手に見てくれるので、キーの指定を省略。(ただしこの問題では start_time または end_time のどちらかで)


```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort by start_time, end_time
        intervals.sort()
        
        # pop the first interval
        results = [intervals.pop(0)]
        
        # traverse other intervals
        for start_time, end_time in intervals:
            
            # If the interval starts before the previous end time,
            # merge them.
            if (start_time <= results[-1][1]):
                results[-1][1] = max(results[-1][1], end_time)
                continue
            
            # New interval
            results.append([start_time, end_time])
        return results
```

-----------------------

## step3 end_time でソートしてみる

## 時間
7分

## 時間計算量: O(n log n)
step1と同じなので省略

## 空間計算量: O(n) 
step1と同じなので省略

## 変更点

せっかくなので、終了時間でソートしてみる。
step2 の `pop(0)`だと、`O(n)` のシフトが発生するが、`pop()`だと `O(1)` で行けるので気持ち早い。

```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort by the end time
        intervals.sort(key = lambda x: x[1])
        
        results = []
        
        later_interval = intervals.pop()
        while (intervals):
            # If the interval starts before the later interval start_time,
            # merge them.
            start_time, end_time = intervals.pop()
            if (later_interval[0] <= end_time):
                later_interval[0] = min(start_time, later_interval[0])
                continue
            
            results.append(later_interval)
            later_interval = [start_time, end_time]
            
        results.append(later_interval)
        return results
```

ちなみに `intervals.pop()` をしなければ、気持ち早くなるかなと思ったけど、実行速度として大差はなかった。

```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort by the end time
        intervals.sort(key = lambda x: x[1])
        
        results = []
        
        num_of_intervals = len(intervals)
        later_interval = intervals[-1]
        
        for i in range(num_of_intervals - 2, -1, -1):
            
            start_time, end_time = intervals[i]
            if (later_interval[0] <= end_time):
                later_interval[0] = min(start_time, later_interval[0])
                continue
            
            results.append(later_interval)
            later_interval = [start_time, end_time]
            
        results.append(later_interval)
        return results
```