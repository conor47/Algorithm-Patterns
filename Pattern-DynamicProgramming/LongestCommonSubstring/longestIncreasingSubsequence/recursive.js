// Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

// Example 1:

// Input: {4,2,3,6,10,1,12}
// Output: 5
// Explanation: The LIS is {2,3,6,10,12}.

// Example 1:

// Input: {-4,10,3,7,15}
// Output: 4
// Explanation: The LIS is {-4,3,7,15}.

const findLISLength = function (nums) {
  const recursive = function (nums, previousIndex, currentIndex) {
    if (currentIndex === nums.length) {
      return 0;
    }

    let c1 = 0;
    if (previousIndex === -1 || nums[currentIndex] > nums[previousIndex]) {
      c1 = 1 + recursive(nums, currentIndex, currentIndex + 1);
    }

    let c2 = recursive(nums, currentIndex, currentIndex + 1);

    return Math.max(c1, c2);
  };
  return recursive(nums, -1, 0);
};

// Time complexity is O(2^N) where N is the length of the input array

// Space complexity is O(N) for the recursion stack

console.log(
  `Length of Longest Increasing Subsequence: ---> ${findLISLength([
    4, 2, 3, 6, 10, 1, 12,
  ])}`
);
console.log(
  `Length of Longest Increasing Subsequence: ---> ${findLISLength([
    -4, 10, 3, 7, 15,
  ])}`
);
