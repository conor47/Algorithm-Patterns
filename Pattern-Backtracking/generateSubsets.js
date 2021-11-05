// Given a set with distinct elements, find all of its distinct subsets.

// Example 1:

// Input: [1, 3]
// Output: [], [1], [3], [1,3]

// Example 2:

// Input: [1, 5, 3]
// Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

const find_subsets = function (nums) {
  if (nums.length === 0) return [];
  let result = [[]];

  const backtrack = (index, current) => {
    for (let i = index; i < nums.length; i++) {
      current.push(nums[i]);
      result.push([...current]);
      backtrack(i + 1, current);
      current.pop();
    }
  };
  backtrack(0, []);
  return result;
};

// In each step the number of subsets doubles as we add the number to all existing subsets. We will have O(2^N) subsets where N is the
// number of elements in input set. Since we are building a new subset for each set the total time complexity is O(N * 2^N)

// Space complexity is O(N * 2^N) too

console.log(find_subsets([1, 5, 3]));
