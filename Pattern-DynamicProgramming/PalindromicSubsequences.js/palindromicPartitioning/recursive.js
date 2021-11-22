// Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

// Example 1:

// Input: "abdbca"
// Output: 3
// Explanation: Palindrome pieces are "a", "bdb", "c", "a".

// Example 2:

// Input: = "cddpd"
// Output: 2
// Explanation: Palindrome pieces are "c", "d", "dpd".

// Example 3:

// Input: = "pqr"
// Output: 2
// Explanation: Palindrome pieces are "p", "q", "r".

// Example 4:

// Input: = "pp"
// Output: 0
// Explanation: We do not need to cut, as "pp" is a palindrome.

const findMPPCuts = function (str) {
  function recursive(str, start, end) {
    if (start >= end || isPalindrome(str, start, end)) {
      return 0;
    }

    let minCuts = end - start;
    for (let i = start; i <= end; i++) {
      if (isPalindrome(str, start, i)) {
        minCuts = Math.min(minCuts, 1 + recursive(str, i + 1, end));
      }
    }
    return minCuts;
  }

  return recursive(str, 0, str.length - 1);
};

const isPalindrome = function (str, x, y) {
  while (x <= y) {
    if (str[x++] !== str[y--]) {
      return false;
    }
  }
  return true;
};

// Time complexity is O(2^n)

// Space complexity is O(n)

console.log(`Minimum palindrome partitions ---> ${findMPPCuts('abdbca')}`);
console.log(`Minimum palindrome partitions ---> ${findMPPCuts('cdpdd')}`);
console.log(`Minimum palindrome partitions ---> ${findMPPCuts('pqr')}`);
console.log(`Minimum palindrome partitions ---> ${findMPPCuts('pp')}`);
