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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const head = new ListNode(-1);
  let tail = head;
  let carryUp = 0;
  while (l1 || l2 || carryUp > 0) {
      const sum = carryUp + (l1?.val || 0) + (l2?.val || 0);
      tail.next = new ListNode(sum % 10);
      tail = tail.next;
      carryUp = Math.floor(sum / 10);
      if (l1) {
          l1 = l1.next;
      }
      if (l2) {
          l2 = l2.next;
      }
  }
  return head.next;
};