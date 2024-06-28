"""
# step1: 思い付いたコードで書く

UnionFindで解いた記憶があるものの面倒そうなので、とりあえず 1 を見つけたら、その島のサイズを調べに行くシンプルな方法で解いた。

## 時間計算量: O(M * N)
M ... grid.length
N ... grid[0].length

## 空間計算量: O(M * N)
全て`1`の場合、`getIslandSize()` のキューの最大サイズは `M * N - 1`になる。`-1`は開始地点。

## メモ
getIslandSize() は、シンプルにdfs() でも良かったかも。
"""

from typing import List

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        result = 0
        for y in range(M):
            for x in range(N):
                # 1でなければ次に移動
                if grid[y][x] != 1:
                    continue
                # 1を見つけたら、2に一時的に書き換える
                grid[y][x] = 2
                result = max(result, self.getIslandSize(grid, y, x))
        
        # お行儀よく、2→1に戻しておく
        for y in range(M):
            for x in range(N):
                if grid[y][x] != 2:
                    continue
                grid[y][x] = 1
                
        return result
    
    def getIslandSize(self, grid: List[List[int]], y: int, x: int) -> int:
        # キューが空になるまで探索を行う。再帰呼出しをしないので、
        # スタックが作成されない分だけ早い。(stack overflowも起こさない)
        queue = [[y, x]]
        result = 1
        M, N = len(grid), len(grid[0])
        while queue:
            pos_y, pos_x = queue.pop(0)
            
            # 上下左右をチェック
            for dy, dx in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                if dy == 0 and dx == 0:
                    continue

                # 上下左右の移動先を計算。
                # if (0 < dst_x < N) でも良いが
                # max(min())の方が if文をシンプルに書けるので
                # 最近はこうしている
                dst_y = max(min(pos_y + dy, M - 1), 0)
                dst_x = max(min(pos_x + dx, N - 1), 0)
                if grid[dst_y][dst_x] != 1:
                    continue

                # 1の場合、キューに追加して継続する
                grid[dst_y][dst_x] = 2
                queue.append([dst_y, dst_x])
                result += 1
        return result
