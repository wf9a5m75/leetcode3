/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function sortList(head: ListNode | null): ListNode | null {
    if (!head) {
        return null;
    }

    const buffer: ListNode[] = [];
    let headNext: ListNode | null;
    while (head) {
        headNext = head.next;
        head.next = null;
        buffer.push(head);
        head = headNext;
    }

    buffer.sort((a, b) => a.val - b.val);

    head = buffer[0];
    let tail = head;
    let i = 0;
    while (i < buffer.length) {
        tail.next = buffer[i];
        tail = tail.next;
        i++;
    }
    tail.next = null;
    return head;
};