// You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

// We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

// Return the reformatted license key.

// Example 1:

// Input: s = "5F3Z-2e-9-w", k = 4
// Output: "5F3Z-2E9W"
// Explanation: The string s has been split into two parts, each part has 4 characters.
// Note that the two extra dashes are not needed and can be removed.

const licenseKeyFormatting = function (s, k) {
  let result = '';
  let chars = s.split('');
  let count = 0;
  let i = chars.length - 1;

  while (i >= 0) {
    if (chars[i] === '-') {
      i -= 1;
    } else if (count !== 0 && count % k === 0) {
      result = '-' + result;
      count = 0;
    } else {
      result = chars[i] + result;
      i -= 1;
      count += 1;
    }
  }
  return result.toUpperCase();
};

// time complexity is O(N) where n is the length of the input string

// Space complexity is O(N)
