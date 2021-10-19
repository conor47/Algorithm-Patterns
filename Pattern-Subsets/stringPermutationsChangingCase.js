// Given a string, find all of its permutations preserving the character sequence but changing case.

// Example 1:

// Input: "ad52"
// Output: "ad52", "Ad52", "aD52", "AD52"

// Example 2:

// Input: "ab7c"
// Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

const find_letter_case_string_permutations = function (str) {
  permutations = [];
  permutations.push(str);
  for (let i = 0; i < str.length; i++) {
    if (isNaN(parseInt(str[i], 10))) {
      let n = permutations.length;
      for (let j = 0; j < n; j++) {
        let chars = permutations[j].split('');

        if (chars[i] === chars[i].toLowerCase()) {
          chars[i] = chars[i].toUpperCase;
        } else {
          chars[i] = chars[i].toLowerCase;
        }
        permutations.push(chars.join(''));
      }
    }
  }
  return permutations;
};

// Time complexity : Since we can have 2^n permutations at most and we are converting each into an array the time complexity is O(N * 2^N)

// Space complexity is O(N * 2^N) since we have 2^N possible permutations and each is N chars long

console.log(
  `String permutations are: ${find_letter_case_string_permutations('ad52')}`
);
console.log(
  `String permutations are: ${find_letter_case_string_permutations('ab7c')}`
);
