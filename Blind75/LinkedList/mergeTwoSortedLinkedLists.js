// Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

let mergeTwoLists = function (l1, l2) {
  let preHead = ListNode(-1);
  let prev = preHead;
  while (l1 && l2) {
    if (l1.val <= l2.val) {
      prev.next = l1;
      l1 = l1.next;
    } else {
      prev.next = l2;
      l2 = l2.next;
    }
    prev = prev.next;
  }
  if (l1 !== null) {
    prev.next = l1;
  } else {
    prev.next = l2;
  }

  return preHead.next;
};

// time complexity is O(n + m)

// space complexity is O(1)

// recursive solution

let mergeRecursive = function (l1, l2) {
  if (l1 === null) return l2;
  else if (l2 === null) return l1;
  else if (l1.val <= l2.val) {
    l1.next = mergeRecursive(l1.next, l2);
    return l1;
  } else {
    l2.next = mergeRecursive(l1, l2.next);
    return l2;
  }
};
