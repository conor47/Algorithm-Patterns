const addTwoNumbers = function (l1, l2) {
  let dummyHead = new ListNode(0);
  let current = dummyHead;

  let p = l1;
  let q = l2;

  let carry = 0;
  while (p !== null || q !== null) {
    let x = p === null ? 0 : p.val;
    let y = q === null ? 0 : q.val;
    let sum = x + y + carry;
    carry = Math.floor(sum / 10);
    current.next = new ListNode(sum % 10);
    current = current.next;
    if (p !== null) p = p.next;
    if (q !== null) q = q.next;
  }

  if (carry > 0) {
    current.next = new ListNode(carry);
  }

  return dummyHead.next;
};

// Time complexity is O(max(M,N)) where M and N are the lengths of the linked lists

// Space complexity is O(max(M,N)) since the new linked list is at max O(max(N,M)) + 1
