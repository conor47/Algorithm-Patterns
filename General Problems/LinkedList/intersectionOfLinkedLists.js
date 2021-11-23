// Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null

// Constraints:

//     The number of nodes of listA is in the m.
//     The number of nodes of listB is in the n.
//     0 <= m, n <= 3 * 104
//     1 <= Node.val <= 105
//     0 <= skipA <= m
//     0 <= skipB <= n
//     intersectVal is 0 if listA and listB do not intersect.
//     intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

// Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?

var getIntersectionNode = function (headA, headB) {
  if (headA === null || headB === null) return null;
  visisted = new Map();

  let temp = headA;
  while (temp) {
    visisted.set(temp, 1);
    temp = temp.next;
  }

  temp = headB;
  while (temp) {
    if (visisted.has(temp)) {
      return temp;
    }
    temp = temp.next;
  }
  return null;
};

// Time complexity is O(M + N) where M and N are the length of the linked lists

// Space complexity is O(M) since we are keeping a map of all the nodes in the first linked list
