function licenseKeyFormatting(s: string, k: number): string {
    const buffer: string[] = s.toUpperCase().replaceAll('-', '').split('');
    const results: string[] = [];
    let i = buffer.length - 1;
    while (i >= 0) {
        let j = Math.max(i - k, -1);
        while (i > j) {
            results.push(buffer.pop()!);
            i--;
        }
        if (i >= 0) {
            results.push('-');
        }
    }
    return results.reverse().join('');
};