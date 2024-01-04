class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m, n = len(bank), len(bank[0])
        
        beams = 0
        prev = 0
        for y in range(m):

            # Find security devices in the current row
            curr = 0
            for x in range(n):
                curr += 1 if bank[y][x] == "1" else 0
            
            # If no security device in the current row,
            # the laser beams through on this row.
            # Skip the calculation.
            if (curr == 0):
                continue

            # summation
            beams += prev * curr
            prev = curr
        return beams