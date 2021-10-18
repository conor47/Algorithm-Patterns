// Given a set of numbers that might contain duplicates, find all of its distinct subsets.

// Example 1:

// Input: [1, 3, 3]
// Output: [], [1], [3], [1,3], [3,3], [1,3,3]

// Example 2:

// Input: [1, 5, 3, 3]
// Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

const find_subsets = function (nums) {
  subsets = [];
  // The nums array is first sorted
  nums.sort((a, b) => a - b);
  subsets.push([]);

  let startIndex = 0;
  let endIndex = 0;
  for (let i = 0; i < nums.length; i++) {
    startIndex = 0;
    // If the num is a duplicate only add the current num to all of the subsets created in the previous step
    if (i > 0 && nums[i] === nums[i - 1]) {
      startIndex = endIndex + 1;
    }
    endIndex = subsets.length - 1;
    for (let j = startIndex; j < endIndex + 1; j++) {
      let newSet = subsets[j].slice(0);
      newSet.push(nums[i]);
      subsets.push(newSet);
    }
  }
  return subsets;
};

// Time complexity is O(N * 2^N) for the same reasoning as in the subsets problem

// Space complexity is also O(N * 2^n) since we will have a total of 2^n subsets each of which can take up O(N) space

console.log(find_subsets([1, 3, 3]));
console.log(find_subsets([1, 5, 3, 3]));
