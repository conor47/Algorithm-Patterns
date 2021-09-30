// Given a string, find the length of the longest substring, which has all distinct characters.

// Example 1:

// Input: String="aabccbb"
// Output: 3
// Explanation: The longest substring with distinct characters is "abc".

// Example 2:

// Input: String="abbbb"
// Output: 2
// Explanation: The longest substring with distinct characters is "ab".

// Example 3:

// Input: String="abccde"
// Output: 3
// Explanation: Longest substrings with distinct characters are "abc" & "cde".

function longestDistinct(str) {
  let charFrequency = {};
  let longest = 0;
  let windowStart = 0;

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    let rightChar = str[windowEnd];

    if (rightChar in charFrequency) {
      // if windowStart is already ahead of the last position of rightChar we keep its position. If its not then we move it to the
      // position after the last postiion of rightChar
      windowStart = Math.max(windowStart, charFrequency[rightChar] + 1);
    }

    charFrequency[rightChar] = windowEnd;
    longest = Math.max(longest, windowEnd - windowStart + 1);
  }
  return longest;
}

const result = longestDistinct('aabccbb');
console.log(result);
