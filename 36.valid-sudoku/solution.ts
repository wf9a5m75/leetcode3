function isValidSudoku(board: string[][]): boolean {
    
    // key: board index (0 - 8)
    // value: bit flags (0 to 8 bit)
    const partialBoards: number[] = Array(9).fill(0);
    
    const rows: number[] = Array(0).fill(0);
    const cols: number[] = Array(0).fill(0);
    
    for (let y = 0; y < 9; y++) {
        for (let x = 0; x < 9; x++) {
            const boardIdx = Math.floor(y / 3) * 3 + Math.floor(x / 3);
            
            const cell: string = board[y][x];
            if (cell === ".") {
                continue;
            }
            
            const cellVal = parseInt(cell, 10);
            const bitMask = 1 << (cellVal - 1);
            
            // Check the cellVal does not appear in the same partial board.
            if ((partialBoards[boardIdx] & bitMask) !== 0) {
                return false;
            }
            partialBoards[boardIdx] |= bitMask;
            
            // Check the cellVal does not appear in the same column.
            if ((cols[x] & bitMask) !== 0) {
                return false;
            }
            cols[x] |= bitMask;
            
            // Check the cellVal does not appear on the same row.
            if ((rows[y] & bitMask) !== 0) {
                return false;
            }
            rows[y] |= bitMask;
        }
    }
    return true;
};