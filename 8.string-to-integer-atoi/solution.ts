function myAtoi(s: string): number {
    const n = s.length;
    
    let idx = 0;
    // skip white speace.
    while (idx < n && s[idx] === ' ') {
        idx++;
    }
    if (idx === n) {
        return 0;
    }

    const isNegativeValue = s[idx] === '-';
    if (isSign(s[idx])) {
        idx++;
    }

    const codeZero = '0'.charCodeAt(0);
    let value = 0;
    while (idx < n && isDigit(s[idx])) {
        value = value * 10 + (s.charCodeAt(idx) - codeZero);
        idx++;
    }
    if (isNegativeValue) {
        value = value * -1;
    }
    const lower_bound = -Math.pow(2, 31);
    const upper_bound = Math.pow(2, 31) - 1;
    return Math.min(Math.max(value, lower_bound), upper_bound);
};

function isDigitOrSign(char: string): boolean {
    return isDigit(char[0]) || isSign(char[0]);
}
function isDigit(char: string): boolean {
    return /^[0123456789]$/.test(char);
}
function isSign(char: string): boolean {
    return char === "+" || char === "-";
}