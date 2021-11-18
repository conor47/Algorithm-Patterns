// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Example 2:

// Input: strs = [""]
// Output: [[""]]

// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]

// Constraints:

//     1 <= strs.length <= 104
//     0 <= strs[i].length <= 100
//     strs[i] consists of lowercase English letters.

const groupAnagrams = function (strs) {
  let frequency = new Map();
  let result = [];
  for (let str of strs) {
    let sorted = str.split('').sort().join('');
    if (!frequency.has(sorted)) {
      frequency.set(sorted, []);
    }
    frequency.get(sorted).push(str);
  }

  for (let val of frequency.values()) {
    result.push(val);
  }
  return result;
};

// Time complexity is O(NK Log K) where N is the lenght of strs and K is the length
// of the longest string in strs. This is due to sorting each string

// Space complexity is O(NK) since in frequency we are storing N strings of
// size K as most.
