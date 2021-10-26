// Given a string and a pattern, find out if the string contains any permutation of the pattern.

// Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

//     abc
//     acb
//     bac
//     bca
//     cab
//     cba

// If a string has ‘n’ distinct characters, it will have n!n!n! permutations.

// Example 1:

// Input: String="oidbcaf", Pattern="abc"
// Output: true
// Explanation: The string contains "bca" which is a permutation of the given pattern.

// Example 2:

// Input: String="odicf", Pattern="dc"
// Output: false
// Explanation: No permutation of the pattern is present in the given string as a substring.

// Example 3:

// Input: String="bcdxabcdy", Pattern="bcdyabcdx"
// Output: true
// Explanation: Both the string and the pattern are a permutation of each other.

// Example 4:

// Input: String="aaacb", Pattern="abc"
// Output: true
// Explanation: The string contains "acb" which is a permutation of the given pattern.

const find_permutation = function (str, pattern) {
  let charFrequency = {};

  // build up char frequency object of chars in pattern
  for (let i = 0; i < pattern.length; i++) {
    if (pattern[i] in charFrequency) {
      charFrequency[pattern[i]] += 1;
    } else {
      charFrequency[pattern[i]] = 1;
    }
  }

  let windowStart = 0;
  let matches = 0;

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    let rightChar = str[windowEnd];

    if (rightChar in charFrequency) {
      charFrequency[rightChar] -= 1;
      if (charFrequency[rightChar] === 0) {
        matches += 1;
      }
    }

    // if this condition is met that we matched the pattern
    if (matches === Object.keys(charFrequency).length) {
      return true;
    }

    if (windowEnd >= pattern.length - 1) {
      let leftChar = str[windowStart];
      windowStart += 1;
      if (leftChar in charFrequency) {
        if (charFrequency[leftChar] === 0) {
          matches -= 1;
        }
        charFrequency[leftChar] += 1;
      }
    }
  }
  return false;
};

// time complexity is O(n + m) where n and m are the character counts of the string and pattern respectively

// space complexity is O(m) since in the worst case the pattern can have all distinct chars

console.log(`Permutation exist: ${find_permutation('oidbcaf', 'abc')}`);
console.log(`Permutation exist: ${find_permutation('odicf', 'dc')}`);
console.log(`Permutation exist: ${find_permutation('bcdxabcdy', 'bcdyabcdx')}`);
console.log(`Permutation exist: ${find_permutation('aaacb', 'abc')}`);
