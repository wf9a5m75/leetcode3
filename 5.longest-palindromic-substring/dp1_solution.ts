function longestPalindrome(s: string): string {
    const n = s.length;
    const dp: number[][] = Array(n).fill(null).map(_row => {
        return Array(n).fill(0);
    });

    // All single characters become one palindrome at leat.
    let ansStart = 0;
    let ansEnd = 0;
    let maxLength = 1;
    for (let i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // If the same characters are consecutive, it's palindrome.
    for (let i = 0; i < n; i++) {
        if (s[i] !== s[i + 1]) {
            continue;
        }
        dp[i][i + 1] = 1;
        ansStart = i;
        ansEnd = i + 1;
        maxLength = 2;
    }

    // From here, we will check k steps
    let k = 0;
    while (k < n) {
        let i = 0;
        while ((i < n - 1) && (i < k)) {
            if (dp[i + 1][k - 1] > 0 && s[i] === s[k]) {
                // Put the same character at the mirroring position.
                dp[i][k] = dp[i + 1][k - 1];
            }

            if (dp[i][k] > 0 && (k - i + 1 > maxLength)) {
                ansStart = i;
                ansEnd = k;
                maxLength = ansEnd - ansStart + 1;
            }
            i++;
        }
        k++;
    }

    // dp.forEach(row => console.log(row));
    return s.substring(ansStart, ansEnd + 1);
}