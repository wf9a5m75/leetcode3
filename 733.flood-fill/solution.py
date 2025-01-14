class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = [(sr, sc)]
        pick_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        checked = set()

        while q:
            r, c = q.pop(0)
            key = f"{r}{c}"
            if key in checked:
                continue
            checked.add(key)
            image[r][c] = color

            for dy, dx in directions:
                key = f"{r + dy}{c + dx}"
                y = r + dy
                x = c + dx
                if (y < 0 or y == rows or
                    x < 0 or x == cols or
                    key in checked or 
                    image[y][x] != pick_color):
                    continue
                q.append((y, x))
        return image
