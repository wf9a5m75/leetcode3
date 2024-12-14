"""
# step2: UnionFindで解けるはずなので、試してみた

## 時間計算量: O(M * N)
M ... grid.length
N ... grid[0].length

## 空間計算量: O(M * N)

## メモ
- Union-Findがウル覚えで2時間掛かった（あと深夜なので、やや頭が回っていない）
- 次回はdfsでやろう、と決意。
"""
from typing import List, Mapping
from collections import defaultdict

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        # 島がどの親IDに所属するかを保持する。
        #     key: 島のid
        #     value: 島のidの親id
        parents = {}
        
        # 島のサイズ
        #    key: 島のid
        #    value: サイズ
        islands = defaultdict(int)
        
        # 次に割り当てる島のid。
        # grid[y][x] には 0 or 1が入っているので、存在しない値 2以上を用いる
        next_island_id = 2
        
        # 一番大きな島のサイズ
        result = 0
        
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 0:
                    continue

                # 新しい島を見つけたら、新しいidを割り当てる
                if grid[y][x] == 1:
                    grid[y][x] = next_island_id
                    islands[next_island_id] = 1
                    parents[next_island_id] = next_island_id
                    result = max(result, islands[next_island_id])
                    next_island_id += 1
                
                # 下と右のセルをチェックする。
                for dy, dx in [[1, 0], [0, 1]]:
                    dst_y = max(min(y + dy, M - 1), 0)
                    dst_x = max(min(x + dx, N - 1), 0)
                        
                    if grid[dst_y][dst_x] == 0:
                        continue
                    
                    # もし 1なら、同じ島としてカウントする。
                    if grid[dst_y][dst_x] == 1:
                        parent_id = self.findRoot(parents, grid[y][x])
                        grid[dst_y][dst_x] = parent_id
                        islands[parent_id] += 1
                        result = max(result, islands[parent_id])
                        continue

                    # もし 2以上なら、別の島と繋がっているので、
                    # idが大きい数値の方にサイズを加算する。
                    # (union処理)
                    parent_id1 = self.findRoot(parents, grid[dst_y][dst_x])
                    parent_id2 = self.findRoot(parents, grid[y][x])
                    if parent_id1 == parent_id2:
                        continue
                    lower_id = min(parent_id1, parent_id2)
                    higher_id = max(parent_id1, parent_id2)

                    islands[higher_id] += islands[lower_id]
                    islands[lower_id] = 0
                    parents[higher_id] = higher_id
                    parents[lower_id] = higher_id
                    result = max(result, islands[higher_id])
        return result
    
    def findRoot(self, parents: Mapping[int, int], parent_id: int) -> int:
        while (parent_id != parents[parent_id]):
            next_parent_id = parents[parents[parent_id]]
            parents[parent_id] = next_parent_id
            parent_id = next_parent_id
        return parent_id
