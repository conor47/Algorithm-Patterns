// You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

// Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

// Return intervals after the insertion.

let insert = function (intervals, newInterval) {
  if (intervals.length === 0) return [newInterval];
  let merged = [];
  let i = 0;
  while (i < intervals.length && intervals[i][1] < newInterval[0]) {
    merged.push(intervals[i]);
    i += 1;
  }
  while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i += 1;
  }
  merged.push(newInterval);

  while (i < intervals.length) {
    merged.push(intervals[i]);
    i += 1;
  }
  return merged;
};

// time complexity is O(N)

// space complexity is O(N)
