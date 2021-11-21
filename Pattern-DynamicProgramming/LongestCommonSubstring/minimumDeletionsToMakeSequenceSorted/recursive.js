// Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

// Example 1:

// Input: {4,2,3,6,10,1,12}
// Output: 2
// Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.

// Example 2:

// Input: {-4,10,3,7,15}
// Output: 1
// Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.

// Example 3:

// Input: {3,2,1,0}
// Output: 3
// Explanation: Since the elements are in reverse order, we have to delete all except one to get a
// sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}

const findMinimumDeletions = function (nums) {
  const recursive = function (nums, prev, curr) {
    if (curr === nums.length) {
      return 0;
    }

    let c1 = 0;
    if (prev === -1 || nums[curr] > nums[prev]) {
      c1 = 1 + recursive(nums, curr, curr + 1);
    }

    let c2 = recursive(nums, prev, curr + 1);
    return Math.max(c1, c2);
  };
  let longest = recursive(nums, -1, 0);
  return nums.length - longest;
};

// Time complexity is O(2^n) where N is the length of the input array

// Space complexity is O(N) for the recursion stack

console.log(
  `Minimum deletion needed: ---> ${findMinimumDeletions([
    4, 2, 3, 6, 10, 1, 12,
  ])}`
);
console.log(
  `Minimum deletion needed: ---> ${findMinimumDeletions([-4, 10, 3, 7, 15])}`
);
console.log(
  `Minimum deletion needed: ---> ${findMinimumDeletions([3, 2, 1, 0])}`
);
