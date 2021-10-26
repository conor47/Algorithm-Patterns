// Given a string and a pattern, find all anagrams of the pattern in the given string.

// Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N!N! permutations (or anagrams) of a string having NNN characters. For example, here are the six anagrams of the string “abc”:

//     abc
//     acb
//     bac
//     bca
//     cab
//     cba

// Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

// Example 1:

// Input: String="ppqp", Pattern="pq"
// Output: [1, 2]
// Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

// Example 2:

// Input: String="abbcabc", Pattern="abc"
// Output: [2, 3, 4]
// Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

const find_string_anagrams = function (str, pattern) {
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
  let count = 0;

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    let rightChar = str[windowEnd];

    if (rightChar in charFrequency) {
      charFrequency[rightChar] -= 1;
      if (charFrequency[rightChar] === 0) {
        matches += 1;
      }
    }

    if (matches === Object.keys(charFrequency).length) {
      count += 1;
    }

    if (windowEnd - windowStart >= pattern.length - 1) {
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
  return count;
};

// time complexity is O(N + M) where N and M are the lengths of the input string and pattern

// Space complexity is O(M) since in the worst case every char in the pattern in unique and we must store each char in the hashmap.

console.log(find_string_anagrams('ppqp', 'pq'));
console.log(find_string_anagrams('abbcabc', 'abc'));
