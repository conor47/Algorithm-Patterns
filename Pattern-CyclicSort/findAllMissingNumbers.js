// We are given an unsorted array containing numbers taken from the range 1 to ānā. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

// Example 1:

// Input: [2, 3, 1, 8, 2, 3, 5, 1]
// Output: 4, 6, 7
// Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

// Example 2:

// Input: [2, 4, 1, 2]
// Output: 3

// Example 3:

// Input: [2, 3, 2, 1]
// Output: 4

const find_missing_numbers = function (nums) {
  missingNumbers = [];
  let i = 0;
  while (i < nums.length) {
    let j = nums[i] - 1;
    if (nums[i] !== nums[j]) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
    } else {
      i += 1;
    }
  }

  for (i = 0; i < nums.length; i++) {
    if (nums[i] !== i + 1) {
      missingNumbers.push(i + 1);
    }
  }
  return missingNumbers;
};

console.log(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]));
console.log(find_missing_numbers([2, 4, 1, 2]));
console.log(find_missing_numbers([2, 3, 2, 1]));
