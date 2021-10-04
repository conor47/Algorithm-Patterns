// We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

// Example 1:

// Input: [4, 0, 3, 1]
// Output: 2

// Example 2:

// Input: [8, 3, 5, 2, 4, 6, 0, 1]
// Output: 7

const find_missing_number = function (nums) {
  let i = 0;
  while (i < nums.length) {
    let j = nums[i];
    if (nums[i] !== nums[j] && nums[i] < nums.length) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
    } else {
      i += 1;
    }
  }

  for (i = 0; i < nums.length; i++) {
    if (nums[i] !== i) {
      return i;
    }
  }
  return -1;
};

// Time complexity is O(N). In the while loop we are not increment I while swapping thus we may have more than n interations of the loop.
// In the worst cae the while loop will swap n-1 numbers and once a number is at the correct index we increment i.
// The Overall time complexity is O(N) + O(N-1)

// Space complexity is O(1)

console.log(find_missing_number([4, 0, 3, 1]));
console.log(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]));
