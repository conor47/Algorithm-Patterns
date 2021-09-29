// Given a string, find the length of the longest substring in it with no more than K distinct characters.

// Example 1:

// Input: String="araaci", K=2
// Output: 4
// Explanation: The longest substring with no more than '2' distinct characters is "araa".

// Example 2:

// Input: String="araaci", K=1
// Output: 2
// Explanation: The longest substring with no more than '1' distinct characters is "aa".

// Example 3:

// Input: String="cbbebi", K=3
// Output: 5
// Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

// Example 4:

// Input: String="cbbebi", K=10
// Output: 6
// Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

function longestKDistinct(str, k) {
  let longest = 0;
  let charFrequency = {};
  let windowStart = 0;

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    let rightChar = str[windowEnd];
    if (!(rightChar in charFrequency)) {
      charFrequency[rightChar] = 0;
    }
    charFrequency[rightChar] += 1;

    //   we now shrink the sliding window until we are left with k distinct characters in the hashmap
    while (Object.keys(charFrequency).length > k) {
      let leftChar = str[windowStart];
      charFrequency[leftChar] -= 1;
      if (charFrequency[leftChar == 0]) {
        delete charFrequency[leftChar];
      }
      windowStart += 1;
    }
    longest = Math.max(longest, windowEnd - windowStart + 1);
  }
  return longest;
}

// Time complexity is O(N) where N is the number of chars in the input string

// Space complexity O(K) as we are storing a maximum of K+1 chars in the hashmap
