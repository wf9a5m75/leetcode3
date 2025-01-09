function threeSum(nums: number[]): number[][] {
    const sorted = nums.sort((a, b) => a - b);
    const indiciesByNumber = new Map<number, number[]>();
    for (let i = 0; i < sorted.length; i++) {
        const indicies: number[] = indiciesByNumber.get(sorted[i]) || [];
        indicies.push(i);
        indiciesByNumber.set(sorted[i], indicies);
    }

    const results: number[][] = [];
    const checkedOnI = new Set<number>();
    for (let i = 0; i < sorted.length - 2; i++) {
        // Skips if sorted[i] is already checked.
        if (checkedOnI.has(sorted[i])) {
            continue;
        }
        checkedOnI.add(sorted[i]);

        const checkedOnJ = new Set<number>();
        for (let j = i + 1; j < sorted.length - 1; j++) {
            // Skips if sorted[j] is already checked.
            if (checkedOnJ.has(sorted[j])) {
                continue;
            }
            checkedOnJ.add(sorted[j]);

            const rest = 0 - sorted[i] - sorted[j];
            if (!indiciesByNumber.has(rest)) {
                continue;
            }
            const indicies = indiciesByNumber.get(rest)!;
            for (let k = 0; k < indicies.length; k++) {
                if (indicies[k] <= j) {
                    continue;
                }
                results.push([
                    sorted[i],
                    sorted[j],
                    sorted[indicies[k]],
                ]);
                break;
            }
        }
    }
    return results;
};