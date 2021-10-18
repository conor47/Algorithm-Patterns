// Design a class to calculate the median of a number stream. The class should have the following two methods:

//     insertNum(int num): stores the number in the class
//     findMedian(): returns the median of all numbers inserted in the class

// If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

// Example 1:

// 1. insertNum(3)
// 2. insertNum(1)
// 3. findMedian() -> output: 2
// 4. insertNum(5)
// 5. findMedian() -> output: 3
// 6. insertNum(4)
// 7. findMedian() -> output: 3.5

const Heap = require('collections/heap');

class MedianOfAStream {
  constructor() {
    this.maxHeap = new Heap([], null, (a, b) => a - b);
    this.minHeap = new Heap([], null, (a, b) => b - a);
  }
  insert_num(num) {
    if (this.maxHeap.length === 0 || this.maxHeap.peek() >= num) {
      this.maxHeap.push(num);
    } else {
      this.minHeap.push(num);
    }

    if (this.maxHeap.length > this.minHeap.length + 1) {
      this.minHeap.push(this.maxHeap.pop());
    } else if (this.maxHeap.length < this.minHeap.length)
      [this.maxHeap.push(this.minHeap.pop())];
    return -1;
  }

  find_median(self) {
    if (this.maxHeap.length === this.minHeap.length) {
      return this.maxHeap.peek() / 2.0 + this.minHeap.peek() / 2.0;
    } else {
      return this.maxHeap.peek();
    }
    return 0.0;
  }
}

// this solution makes use of the collectionsjs module for a heap implementation.

// time compplexity of insert num is O(Log N)
// time complexity of media is O(1)

// space complexity is O(N) since we are storing all of the numbers.

var medianOfAStream = new MedianOfAStream();
medianOfAStream.insert_num(3);
medianOfAStream.insert_num(1);
console.log(`The median is: ${medianOfAStream.find_median()}`);
medianOfAStream.insert_num(5);
console.log(`The median is: ${medianOfAStream.find_median()}`);
medianOfAStream.insert_num(4);
console.log(`The median is: ${medianOfAStream.find_median()}`);
