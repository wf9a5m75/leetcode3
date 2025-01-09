function longestPalindrome(s: string): string {
    const n = s.length;
    const dp: boolean[][] = new Array(n).fill(null).map(_row => {
        return new Array(n).fill(false);
    });

    // All characters can be a single palindrome substring.
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
    }

    let result = s[0];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (s[i] !== s[j]) {
                continue;
            }
            if (!dp[j + 1][i - 1] && i !== j + 1) {
                continue;
            }
            dp[j][i] = true;
            if (i - j + 1 > result.length) {
                result = s.substring(j, i + 1);
            }
        }
    }
    
    return result;
}