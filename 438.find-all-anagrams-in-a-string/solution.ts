function findAnagrams(s: string, p: string): number[] {
    if (s.length < p.length) {
        return [];
    }
    
    const results: number[] = [];
    const aCode = "a".charCodeAt(0);
    let anagram = new Array(26).fill(0);
    for (const char of p) {
        anagram[char.charCodeAt(0) - aCode]++;
    }

    const window = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        if (i - p.length >= 0) {
            const charCode1 = s.charCodeAt(i - p.length) - aCode;
            window[charCode1]--;
        }

        const charCode2 = s.charCodeAt(i) - aCode;
        window[charCode2]++;
        
        let invalid = false;
        for (let j = 0; j < 26; j++) {
            if (window[j] !== anagram[j]) {
                invalid = true;
                break;
            }
        }
        if (!invalid) {
            results.push(i - p.length + 1);
        }
    }
    
    return results;
};