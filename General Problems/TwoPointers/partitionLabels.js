// You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

// Return a list of integers representing the size of these parts.

// Example 1:

// Input: s = "ababcbacadefegdehijhklij"
// Output: [9,7,8]
// Explanation:
// The partition is "ababcbaca", "defegde", "hijhklij".
// This is a partition so that each letter appears in at most one part.
// A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

// Example 2:

// Input: s = "eccbbbbdec"
// Output: [10]

// Constraints:

//     1 <= s.length <= 500
//     s consists of lowercase English letters.

const partitionLabels = function (s) {
  let res = [];
  let lastIndexes = new Map();
  for (let i = 0; i < s.length; i++) {
    lastIndexes.set(s[i], i);
  }

  let i = 0;
  while (i < s.length) {
    let end = lastIndexes.get(s[i]);
    for (let j = i; j <= end; j++) {
      end = Math.max(end, lastIndexes.get(s[j]));
    }
    res.push(end - i + 1);
    i = end + 1;
  }
  return res;
};

// Time complexity O(N)

// Space complexity is (N)
