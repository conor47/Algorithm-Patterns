// Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

// Each number in candidates may only be used once in the combination.

// Note: The solution set must not contain duplicate combinations.

// Example 1:

// Input: candidates = [10,1,2,7,6,1,5], target = 8
// Output:
// [
// [1,1,6],
// [1,2,5],
// [1,7],
// [2,6]
// ]

// Example 2:

// Input: candidates = [2,5,2,1,2], target = 5
// Output:
// [
// [1,2,2],
// [5]
// ]

// Constraints:

//     1 <= candidates.length <= 100
//     1 <= candidates[i] <= 50
//     1 <= target <= 30

const combinationSum2 = function (candidates, target) {
  candidates.sort((a, b) => a - b);
  let result = [];
  recursive(candidates, 0, [], target, result);
  return result;
};

const recursive = function (candidates, index, current, target, result) {
  if (target < 0) {
    return;
  }

  if (target === 0) {
    result.push([...current]);
    return;
  }

  for (let i = index; i < candidates.length; i++) {
    if (i === index || candidates[i] !== candidates[i - 1]) {
      current.push(candidates[i]);
      recursive(candidates, i + 1, current, target - candidates[i], result);
      current.pop();
    }
  }
};

// Time complexity is O(2^N) since in the worst case this algorithm exhausts all
// possible continations of the input array

// Space complexity is O(N) for the recursion stack and for the current array.
