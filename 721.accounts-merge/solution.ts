//
//  N ... accounts.length
//  M ... max(accoutns[i].length)
// 
/

function accountsMerge(accounts: string[][]): string[][] {
    // The email variable has "all emails and all numbers", SC is O(N x M)
    const emails: Map<string, number> = new Map();
    const people: string[][] = [];
    const parent: number[] = [];

    // Due to compress the path, TC is O(1)
    function findParent(parentIdx: number | undefined): number {
        if (parentIdx === undefined || parentIdx === -1) {
            return -1;
        }
        if (parent[parentIdx] === parentIdx) {
            return parentIdx;
        }
        parent[parentIdx] = findParent(parent[parentIdx]);
        return parent[parentIdx];
    }

    // TC is O(N x M)
    for (const [name, ...emailList] of accounts) {
        let lastParentId = -1;
        for (const email of emailList) {
            lastParentId = findParent(lastParentId);
            const parentIdx = findParent(emails.get(email));
            if (lastParentId === -1 && parentIdx === -1) {
                // new person
                lastParentId = parent.length;
                parent.push(lastParentId);
                people.push([name]);
            } else if (lastParentId === -1 && parentIdx !== -1) {
                // exist person
                lastParentId = parentIdx;
            } else if (lastParentId !== -1 && parentIdx === -1) {
                // apply the same personal id
                lastParentId = lastParentId;
            } else {
                // merge two indecies
                const dst = Math.min(lastParentId, parentIdx);
                const src = Math.max(lastParentId, parentIdx);
                parent[src] = dst;
                lastParentId = dst;
            }
            emails.set(email, lastParentId);
        }
    }
    
    // TC is O(N x M)
    for (const [email, parentIdx] of emails.entries()) {
        const root = findParent(parentIdx);
        people[root].push(email);
    }

    // Since we need to sort the email addresses,
    // TC is O(NM log NM)
    // 
    // The worst case is that all email addresses belong to the one group.
    const results: string[][] = [];
    for (let i = 0; i < people.length; i++) {
        const root = findParent(i);
        if (i !== root) {
            continue;
        }
        const name = people[i].shift()!;
        people[i].sort();
        people[i].unshift(name);
        results.push(people[i]);
    }

    return results;
};
