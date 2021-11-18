// Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

// The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

// It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

// Example 1:

// Input: candidates = [2,3,6,7], target = 7
// Output: [[2,2,3],[7]]
// Explanation:
// 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
// 7 is a candidate, and 7 = 7.
// These are the only two combinations.

// Example 2:

// Input: candidates = [2,3,5], target = 8
// Output: [[2,2,2,2],[2,3,3],[3,5]]

// Example 3:

// Input: candidates = [2], target = 1
// Output: []

// Example 4:

// Input: candidates = [1], target = 1
// Output: [[1]]

// Example 5:

// Input: candidates = [1], target = 2
// Output: [[1,1]]

// Constraints:

//     1 <= candidates.length <= 30
//     1 <= candidates[i] <= 200
//     All elements of candidates are distinct.
//     1 <= target <= 500

var combinationSum = function (candidates, target) {
  let result = [];
  backtrack(candidates, target, [], 0, result);
  return result;
};

const backtrack = function (candidates, target, current, index, result) {
  if (target === 0) {
    result.push([...current]);
    return;
  }

  if (target < 0 || index >= candidates.length) {
    return;
  }

  current.push(candidates[index]);
  backtrack(candidates, target - candidates[index], current, index, result);
  current.pop();
  backtrack(candidates, target, current, index + 1, result);
};

// Time complexity is O(N^(T/M + 1))

// Space complexity is O(T/M) where T is the total and M is the smallest element in the candidate array. The number of invocations on the stack
// can reach T/M when continually taking the smallest element. The current array can reach a max lenght of T/M. Together we get a space
// complexity of T/M
