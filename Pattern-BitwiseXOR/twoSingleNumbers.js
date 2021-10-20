// In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

// Example 1:

// Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
// Output: [4, 6]

// Example 2:

// Input: [2, 1, 3, 2]
// Output: [1, 3]

function find_single_numbers(nums) {
  // find the XOR of all the numbers
  let x = 0;
  for (let i = 0; i < nums.length; i++) {
    x ^= nums[i];
  }

  //   find the rightmost bit that is 1. Partition the nums array based on this bit
  let rightMostBit = 1;
  while ((rightMostBit & x) === 0) {
    rightMostBit = rightMostBit << 1;
  }
  let num1 = 0;
  let num2 = 0;

  nums.forEach((num) => {
    if ((num & rightMostBit) !== 0) num1 ^= num;
    else num2 ^= num;
  });
  return [num1, num2];

  return [-1, -1];
}

console.log(
  `Single numbers are: ${find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])}`
);
console.log(`Single numbers are: ${find_single_numbers([2, 1, 3, 2])}`);
