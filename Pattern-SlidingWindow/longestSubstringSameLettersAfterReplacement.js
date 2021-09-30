// Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, find the length of the longest substring having the same letters after replacement.

// Example 1:

// Input: String="aabccbb", k=2
// Output: 5
// Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

// Example 2:

// Input: String="abbcb", k=1
// Output: 4
// Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".

// Example 3:

// Input: String="abccde", k=1
// Output: 3
// Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

function longestReplacement(str, k) {
  let windowStart = 0;
  let frequency = {};
  let longest = 0;
  let maxRepeatLetterCount = 0;

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    let rightChar = str[windowEnd];

    if (!(rightChar in frequency)) {
      frequency[rightChar] = 0;
    }
    frequency[rightChar] += 1;
    maxRepeatLetterCount = Math.max(maxRepeatLetterCount, frequency[rightChar]);

    // we have some letter repeating maxRepeatLetterCount amount of times. If the remaining letters exceed K we need to shrink the window
    // if they equal k we can replace all of them

    if (windowEnd - windowStart + 1 - maxRepeatLetterCount > k) {
      let leftChar = str[windowStart];
      frequency[leftChar] -= 1;
      windowStart += 1;
    }

    longest = Math.max(longest, windowEnd - windowStart + 1);
  }
  return longest;
}

const result = longestReplacement('abbcb', 1);
console.log(result);
