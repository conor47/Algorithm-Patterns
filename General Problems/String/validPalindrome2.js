// Given a string s, return true if the s can be palindrome after deleting at most one character from it.

// Example 1:

// Input: s = "aba"
// Output: true

// Example 2:

// Input: s = "abca"
// Output: true
// Explanation: You could delete the character 'c'.

// Example 3:

// Input: s = "abc"
// Output: false

// Constraints:

//     1 <= s.length <= 105
//     s consists of lowercase English letters.

const validPalindrome = function (s) {
  let left = 0;
  let right = s.length - 1;

  while (left <= right) {
    if (s[left] !== s[right]) {
      return (
        isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1)
      );
    }
    left += 1;
    right -= 1;
  }
  return true;
};

const isPalindrome = function (s, left, right) {
  while (left <= right) {
    if (s[left] !== s[right]) {
      return false;
    }
    left += 1;
    right -= 1;
  }
  return true;
};

// Time complexity is O(N)

// Space complexity is O(1)
