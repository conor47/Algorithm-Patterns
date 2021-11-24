// Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

// Each letter in magazine can only be used once in ransomNote.

// Example 1:

// Input: ransomNote = "a", magazine = "b"
// Output: false

// Example 2:

// Input: ransomNote = "aa", magazine = "ab"
// Output: false

// Example 3:

// Input: ransomNote = "aa", magazine = "aab"
// Output: true

// Constraints:

//     1 <= ransomNote.length, magazine.length <= 105
//     ransomNote and magazine consist of lowercase English letters.

var canConstruct = function (ransomNote, magazine) {
  let chars = new Map();
  for (let char of magazine) {
    if (chars.has(char)) {
      chars.set(char, chars.get(char) + 1);
    } else {
      chars.set(char, 1);
    }
  }

  for (let char of ransomNote) {
    if (!chars.has(char) || chars.get(char) === 0) {
      return false;
    } else {
      chars.set(char, chars.get(char) - 1);
    }
  }
  return true;
};

// Time complexity is O( M) M is the length of the magazine string. It is not O(M + N) since M >= N in all valid cases

// Space complexity is O(1) since our map will never be greater than 26
