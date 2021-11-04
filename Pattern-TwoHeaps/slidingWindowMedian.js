// Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

// Example 1:

// Input: nums=[1, 2, -1, 3, 5], k = 2
// Output: [1.5, 0.5, 1.0, 4.0]
// Explanation: Lets consider all windows of size ‘2’:

//     [1, 2, -1, 3, 5] -> median is 1.5
//     [1, 2, -1, 3, 5] -> median is 0.5
//     [1, 2, -1, 3, 5] -> median is 1.0
//     [1, 2, -1, 3, 5] -> median is 4.0

// Example 2:

// Input: nums=[1, 2, -1, 3, 5], k = 3
// Output: [1.0, 2.0, 3.0]
// Explanation: Lets consider all windows of size ‘3’:

//     [1, 2, -1, 3, 5] -> median is 1.0
//     [1, 2, -1, 3, 5] -> median is 2.0
//     [1, 2, -1, 3, 5] -> median is 3.0

const Heap = require('collections/heap');

class SlidingWindowMedian {
  find_sliding_window_median(nums, k) {
    if (nums.length === 0) return [];
    let minHeap = new Heap([], null, (a, b) => b - a);
    let maxHeap = new Heap([], null, (a, b) => a - b);
    let result = [];

    let windowStart = 0;
    let windowEnd = 0;

    while (windowEnd - windowStart + 1 <= k) {
      this.insert_into_heaps(nums[windowEnd], minHeap, maxHeap);
      windowEnd += 1;
    }

    windowEnd -= 1;

    result.push(this.calculate_median(minHeap, maxHeap));

    while (windowEnd < nums.length - 1) {
      if (nums[windowStart] <= maxHeap.peek()) {
        maxHeap.delete(nums[windowStart]);
      } else {
        minHeap.delete(nums[windowStart]);
      }
      windowEnd += 1;
      windowStart += 1;

      this.insert_into_heaps(nums[windowEnd], minHeap, maxHeap);
      result.push(this.calculate_median(minHeap, maxHeap));
    }

    return result;
  }

  insert_into_heaps(num, minHeap, maxHeap) {
    if (maxHeap.length === 0 || num <= maxHeap.peek()) {
      maxHeap.push(num);
    } else {
      minHeap.push(num);
    }

    if (maxHeap.length > minHeap.length + 1) {
      minHeap.push(maxHeap.pop());
    } else if (maxHeap.length < minHeap.length) {
      maxHeap.push(minHeap.pop());
    }
  }

  calculate_median(minHeap, maxHeap) {
    if (minHeap.length === maxHeap.length) {
      return minHeap.peek() / 2.0 + maxHeap.peek() / 2.0;
    } else {
      return maxHeap.peek();
    }
  }
}

// time complexity is O(N * K). N is the total number of elements in the input array and K is the size of the sliding window
// We are interating through all N elements and doing two things, 1 - inserting and removing elements from heaps of size k, 2 - deleting
// elements from heaps of size k, which equates to deleting a value in an array of length k

// space complexity is O(k) since at any one point we are storing k elements in the heaps

var slidingWindowMedian = new SlidingWindowMedian();
result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2);

console.log(`Sliding window medians are: ${result}`);

slidingWindowMedian = new SlidingWindowMedian();
result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3);
console.log(`Sliding window medians are: ${result}`);
