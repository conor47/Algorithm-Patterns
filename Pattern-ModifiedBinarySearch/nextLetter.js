// Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

// Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

// Write a function to return the next letter of the given ‘key’.

// Example 1:

// Input: ['a', 'c', 'f', 'h'], key = 'f'
// Output: 'h'
// Explanation: The smallest letter greater than 'f' is 'h' in the given array.

// Example 2:

// Input: ['a', 'c', 'f', 'h'], key = 'b'
// Output: 'c'
// Explanation: The smallest letter greater than 'b' is 'c'.

// Example 3:

// Input: ['a', 'c', 'f', 'h'], key = 'm'
// Output: 'a'
// Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

// Example 4:

// Input: ['a', 'c', 'f', 'h'], key = 'h'
// Output: 'a'
// Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.

const search_next_letter = function (letters, key) {
  let start = 0;
  let end = letters.length - 1;
  let n = letters.length;
  while (start <= end) {
    let mid = Math.floor(start + (end - start) / 2);
    // we skip the condition where letters[mid] = the key.
    if (key < letters[mid]) end = mid - 1;
    else start = mid + 1;
  }
  return letters[start % n];
};

console.log(search_next_letter(['a', 'c', 'f', 'h'], 'f'));
console.log(search_next_letter(['a', 'c', 'f', 'h'], 'b'));
console.log(search_next_letter(['a', 'c', 'f', 'h'], 'm'));
