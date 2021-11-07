// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an of the non-overlapping intervals that cover all the intervals in the input.

// Example 1:

// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

// Example 2:

// Input: intervals = [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.

// Constraints:

//     1 <= intervals.length <= 104
//     intervals[i].length == 2
//     0 <= starti <= endi <= 104

let merge = function (intervals) {
  if (intervals.length <= 1) return intervals;
  intervals.sort((a, b) => a[0] - b[0]);
  let start = intervals[0][0];
  let end = intervals[0][1];
  let merged = [];

  for (let i = 1; i < intervals.length; i++) {
    let interval = intervals[i];

    if (interval[0] <= end) {
      end = Math.max(end, interval[1]);
    } else {
      merged.push([start, end]);
      start = interval[0];
      end = interval[1];
    }
  }
  merged.push([start, end]);
  return merged;
};

// time complexity is O(N)

// space complexity is O(N)
