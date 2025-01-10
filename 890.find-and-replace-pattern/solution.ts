function findAndReplacePattern(words: string[], pattern: string): string[] {
    const results: string[] = [];
    for (const word of words) {
        let invalid = false;
        const memo = new Map<string, string>();
        const used = new Set<string>();
        for (let i = 0; !invalid && i < word.length; i++) {
            if (!memo.has(word[i]) && !used.has(pattern[i])) {
                memo.set(word[i], pattern[i]);
                used.add(pattern[i]);
            } else {
                invalid = memo.get(word[i]) !== pattern[i];
            }
        }
        if (!invalid) {
            results.push(word);
        }
    }
    return results;
};