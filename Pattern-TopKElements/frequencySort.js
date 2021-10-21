// Given a string, sort it based on the decreasing frequency of its characters.

// Example 1:

// Input: "Programming"
// Output: "rrggmmPiano"
// Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

// Example 2:

// Input: "abcbab"
// Output: "bbbaac"
// Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.

const heap = require('collections/heap');

const sort_character_by_frequency = function (str) {
  let frequencyCount = {};
  for (let char of str) {
    if (!(char in frequencyCount)) frequencyCount[char] = 1;
    else frequencyCount[char] += 1;
  }

  let maxHeap = new heap([], null, (a, b) => a[0] - b[0]);

  Object.keys(frequencyCount).forEach((key) => {
    maxHeap.push([frequencyCount[key], key]);
  });

  let result = [];
  while (maxHeap.length > 0) {
    [frequency, char] = maxHeap.pop();
    for (let i = 0; i < frequency; i++) {
      result.push(char);
    }
  }

  return result.join('');
};

// time complexity is O(d * logd) where d is the number of distinct chars in the input string. In the worst case is the string is composed
// of entirely unique chars the time complexity is O(n * logn)

// Space complexity is O(n)

console.log(
  `String after sorting characters by frequency: ${sort_character_by_frequency(
    'Programming'
  )}`
);
console.log(
  `String after sorting characters by frequency: ${sort_character_by_frequency(
    'abcbab'
  )}`
);
