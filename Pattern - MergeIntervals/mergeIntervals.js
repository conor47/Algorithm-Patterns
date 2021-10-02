// Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

// Example 1:

// Intervals: [[1,4], [2,5], [7,9]]
// Output: [[1,5], [7,9]]
// Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
// one [1,5].

// Example 2:

// Intervals: [[6,7], [2,4], [5,9]]
// Output: [[2,4], [5,9]]
// Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

// Example 3:

// Intervals: [[1,4], [2,6], [3,5]]
// Output: [[1,6]]
// Explanation: Since all the given intervals overlap, we merged them into one.

class Interval {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  get_interval() {
    return '[' + this.start + ', ' + this.end + ']';
  }
}

const merge = function (intervals) {
  if (intervals.length < 2) return intervals;
  //   we then sort the intervals on the starting point
  intervals.sort((a, b) => a.start - b.start);

  let mergeIntervals = [];
  let start = intervals[0].start;
  let end = intervals[0].end;
  for (let i = 1; i < intervals.length; i++) {
    let interval = intervals[i];
    // overlapping intervals
    if (interval.start < end) {
      end = Math.max(interval.end, end);
    } else {
      // non overlapping intevals. Add the previous interval and reset
      mergeIntervals.push(new Interval(start, end));
      start = interval.start;
      end = interval.end;
    }
  }
  //   add the last interval
  mergeIntervals.push(new Interval(start, end));
  return mergeIntervals;
};

// Time complexity is O(N Log N). Iterating the intervals takes only O(N) time. Sorting the intervals takes O(Log N) time.

// Space complexity is O(N) as we are returning a list containing all of the intervals. Sorting also generally requires additional space.

merged_intervals = merge([
  new Interval(1, 4),
  new Interval(2, 5),
  new Interval(7, 9),
]);
result = '';
for (i = 0; i < merged_intervals.length; i++) {
  result += merged_intervals[i].get_interval() + ' ';
}
console.log(`Merged intervals: ${result}`);

merged_intervals = merge([
  new Interval(6, 7),
  new Interval(2, 4),
  new Interval(5, 9),
]);
result = '';
for (i = 0; i < merged_intervals.length; i++) {
  result += merged_intervals[i].get_interval() + ' ';
}
console.log(`Merged intervals: ${result}`);

merged_intervals = merge([
  new Interval(1, 4),
  new Interval(2, 6),
  new Interval(3, 5),
]);
result = '';
for (i = 0; i < merged_intervals.length; i++) {
  result += merged_intervals[i].get_interval() + ' ';
}
console.log(`Merged intervals: ${result}`);
