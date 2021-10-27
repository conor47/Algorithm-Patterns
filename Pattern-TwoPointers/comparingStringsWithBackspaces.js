// Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

// Example 1:

// Input: str1="xy#z", str2="xzz#"
// Output: true
// Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

// Example 2:

// Input: str1="xy#z", str2="xyz#"
// Output: false
// Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

// Example 3:

// Input: str1="xp#", str2="xyz##"
// Output: true
// Explanation: After applying backspaces the strings become "x" and "x" respectively.
// In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.

// Example 4:

// Input: str1="xywrrmp", str2="xywrrmu#p"
// Output: true
// Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

const backspace_compare = function (str1, str2) {
  let idx1 = str1.length - 1;
  let idx2 = str2.length - 1;
  while (idx1 >= 0 || idx2 >= 0) {
    let str1Idx = nextValidIndex(str1, idx1);
    let str2Idx = nextValidIndex(str2, idx2);

    if (str1Idx < 0 && str2Idx < 0) {
      return true;
    }
    if (str1Idx < 0 || str2Idx < 0) {
      return false;
    }
    if (str1[str1Idx] !== str2[str2Idx]) {
      return false;
    }

    idx1 = str1Idx - 1;
    idx2 = str2Idx - 1;
  }
  return true;
};

const nextValidIndex = function (str, index) {
  let backSpaceCount = 0;
  while (index >= 0) {
    if (str[index] === '#') {
      backSpaceCount += 1;
    } else if (backSpaceCount > 0) {
      backSpaceCount -= 1;
    } else {
      break;
    }
    index -= 1;
  }
  return index;
};

// Time complexity O(M + N) where M and N are the lengths of the input strings

// Space complexity is O(1)

console.log(backspace_compare('xy#z', 'xzz#'));
console.log(backspace_compare('xy#z', 'xyz#'));
console.log(backspace_compare('xp#', 'xyz##'));
console.log(backspace_compare('xywrrmp', 'xywrrmu#p'));
