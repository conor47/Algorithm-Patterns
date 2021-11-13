// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

// Example 1:

// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]

// Example 2:

// Input: temperatures = [30,40,50,60]
// Output: [1,1,1,0]

// Example 3:

// Input: temperatures = [30,60,90]
// Output: [1,1,0]

// This is the naieve solution.
const dailyTemperatures = function (temps) {
  let res = Array(temps.length).fill(0);

  for (let i = 0; i < temps.length - 1; i++) {
    for (let j = i + 1; j < temps.length; j++) {
      if (temps[j] > temps[i]) {
        res[i] = j - i;
        break;
      }
    }
  }
  return res;
};

// Time complexity is O(N^2)

// Space complexity is O(1)

// Monotonic stack approach

const dailyTemperaturesV2 = function (nums) {
  let n = nums.length;
  const ans = Array(n).fill(0);
  const stack = [];

  for (const [idx, val] of nums.entries()) {
    while (stack.length > 0 && stack[stack.length - 1] < val) {
      let prev_day = stack.pop();
      ans[prev_day] = idx - prev_day;
    }
    stack.push(idx);
  }
  return ans;
};

// The worst case time complexity of this algorithm is O(2N). Even though we have a nested while loop each element can only be pushed on
// and popped into the stack one meaning we will have at most N pushes and pops. This runtime is asymtotically equivalent to O(N)

// Space complextiy is (N) as in the worst case all elements are stored in the stack
