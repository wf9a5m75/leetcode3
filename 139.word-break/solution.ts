type Trie = {
    child: {
        [key: string]: Trie;
    },
    eow: boolean;
}
function wordBreak(s: string, wordDict: string[]): boolean {
    const wordTree: Trie = buildTrieTree(wordDict);
    const reached: boolean[] = new Array(s.length + 1).fill(false);

    const q: number[] = [0];
    while (q.length > 0) {
        const i = q.shift()!;
        if (reached[i]) {
            continue;
        }
        reached[i] = true;

        const words = findWords(wordTree, s, i);
        for (const word of words) {
            q.push(i + word.length);
        }
    }

    return reached[s.length];
};
function findWords(root: Trie, s: string, start: number): string[] {
    const words: string[] = [];
    let parent = root;
    let path: string[] = [];
    for (let i = start; i < s.length; i++) {
        const char = s[i];
        if (!(char in parent.child)) {
            break;
        }
        parent = parent.child[char];
        path.push(char);
        if (parent?.eow) {
            words.push(path.join(''));
        }
    }
    return words;
}

function buildTrieTree(wordDict: string[]): Trie {
    const root: Trie = {
        child: {},
        eow: false,
    };

    for (const word of wordDict) {
        let parent = root;
        for (const char of word) {
            if (!(char in parent.child)) {
                parent.child[char] = {
                    child: {},
                    eow: false,
                };
            }
            parent = parent.child[char];
        }
        parent.eow = true;
    }

    return root;
}