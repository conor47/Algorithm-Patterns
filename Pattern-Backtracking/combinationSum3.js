// Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

// Only numbers 1 through 9 are used.
// Each number is used at most once.

// Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

// Example 1:

// Input: k = 3, n = 7
// Output: [[1,2,4]]
// Explanation:
// 1 + 2 + 4 = 7
// There are no other valid combinations.

// Example 2:

// Input: k = 3, n = 9
// Output: [[1,2,6],[1,3,5],[2,3,4]]
// Explanation:
// 1 + 2 + 6 = 9
// 1 + 3 + 5 = 9
// 2 + 3 + 4 = 9
// There are no other valid combinations.

// Example 3:

// Input: k = 4, n = 1
// Output: []
// Explanation: There are no valid combinations.
// Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

// Example 4:

// Input: k = 3, n = 2
// Output: []
// Explanation: There are no valid combinations.

// Example 5:

// Input: k = 9, n = 45
// Output: [[1,2,3,4,5,6,7,8,9]]
// Explanation:
// 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
// There are no other valid combinations.

// Constraints:

// 2 <= k <= 9
// 1 <= n <= 60

const combinationSum3 = function (k, n) {
  let result = [];

  const backtrack = function (current, target, index) {
    if (target === 0 && current.length === k) {
      result.push([...current]);
      return;
    }

    if (current.length > k || target < 0) {
      return;
    }

    for (let i = index; i <= 9; i++) {
      current.push(i);
      backtrack(current, target - i, i + 1);
      current.pop();
    }
  };
  backtrack([], n, 1);
  return result;
};

// See leetcode for time complexity calculation. It is O(9!.K / (9 - k)!)

// Space complexity is O(K). The current array will store up to K elements. The recursion stack will
// store up to k consecutive invocations at any one time
