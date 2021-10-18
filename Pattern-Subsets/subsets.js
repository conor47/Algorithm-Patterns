// Given a set with distinct elements, find all of its distinct subsets.

// Example 1:

// Input: [1, 3]
// Output: [], [1], [3], [1,3]

// Example 2:

// Input: [1, 5, 3]
// Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

const find_subsets = function (nums) {
  subsets = [];
  // push empty subset
  subsets.push([]);
  for (i = 0; i < nums.length; i++) {
    let currnetNum = nums[i];

    let n = subsets.length;
    for (let j = 0; j < n; j++) {
      let newSet = subsets[j].slice(0);
      newSet.push(currnetNum);
      subsets.push(newSet);
    }
  }
  return subsets;
};

// In each step the number of subsets doubles as we add the number to all existing subsets. We will have O(2^N) subsets where N is the
// number of elements in input set. Since we are building a new subset for each set the total time complexity is O(N * 2^N)

// Space complexity is O(N * 2^N) too

console.log(find_subsets([1, 3]));
console.log(find_subsets([1, 5, 3]));
