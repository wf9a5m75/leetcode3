function numUniqueEmails(emails: string[]): number {
    const results = new Set<string>();

    for (let email of emails) {
        // Valid email address must contain one at-mark.
        const atMarks = email.match(/@/);
        if (!atMarks || atMarks.length !== 1) {
            continue;
        }
        let [localName, domain] = email.split('@');

        // Domain names ens with the ".com" suffix
        if (!domain.endsWith('.com')) {
            continue;
        }

        // Domain names must contain at least one character before ".com" suffix
        if (domain.length <= 4) {
            continue;
        }

        // Local names do not start with a '+' character
        if (localName.startsWith('+')) {
            continue;
        }

        // All local and domain names are non-empty
        if (localName.length === 0) {
            continue;
        }

        // All characters after the first plus "+" mark will be ignored.
        localName = localName.replace(/\+.*$/, '');

        // '.' in the local name will be ignored.
        localName = localName.replace(/\./g, '');
        

        const validEmail = `${localName}@${domain}`;
        results.add(validEmail);
    }

    return results.size;
};