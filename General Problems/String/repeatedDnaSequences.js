// The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

//     For example, "ACGAATTCCG" is a DNA sequence.

// When studying DNA, it is useful to identify repeated sequences within the DNA.

// Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

// Example 1:

// Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
// Output: ["AAAAACCCCC","CCCCCAAAAA"]

// Example 2:

// Input: s = "AAAAAAAAAAAAA"
// Output: ["AAAAAAAAAA"]

// Constraints:

//     1 <= s.length <= 105
//     s[i] is either 'A', 'C', 'G', or 'T'.

const findRepeatedDnaSequences = function (s) {
  let res = new Set();
  let frequency = new Map();
  let current = '';
  for (let i = 0; i <= 9 && i <= s.length; i++) {
    current += s[i];
  }
  i = current.length - 1;
  while (i <= s.length) {
    if (current.length === 10 && !frequency.has(current)) {
      frequency.set(current, 1);
    } else if (current.length === 10) {
      res.add(current);
    }
    i += 1;
    current = current.substring(1) + s[i];
  }
  return Array.from(res);
};

// Time complexity is O(N)

// Space complexity is O(N)
