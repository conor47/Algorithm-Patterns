// Given an array of points in a 2D plane, find ‘K’ closest points to the origin.

// Example 1:

// Input: points = [[1,2],[1,3]], K = 1
// Output: [[1,2]]
// Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
// The Euclidean distance between (1, 3) and the origin is sqrt(10).
// Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

// Example 2:

// Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
// Output: [[1, 3], [2, -1]]

const heap = require('collections/heap');

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  get_point() {
    return '[' + this.x + ', ' + this.y + '] ';
  }

  distance_from_origin() {
    return Math.sqrt(this.x * this.x + this.y * this.y);
  }

  compare(other) {
    return this.distance_from_origin() - other.distance_from_origin(other);
  }
}

const find_closest_points = function (points, k) {
  result = [];
  const maxHeap = new heap([], null, (a, b) => a.compare(b));
  for (let i = 0; i < k; i++) {
    maxHeap.push(points[i]);
  }

  for (let i = k; i < points.length; i++) {
    if (
      points[i].distance_from_origin() < maxHeap.peek().distance_from_origin()
    ) {
      maxHeap.pop();
      maxHeap.push(points[i]);
    }
  }
  return maxHeap.toArray();
};

// time complexity is O (n * log k)

// space complexity is O(K) since we are storing k points in the heap

points = find_closest_points(
  [new Point(1, 3), new Point(3, 4), new Point(2, -1)],
  2
);
result = 'Here are the k points closest the origin: ';
for (i = 0; i < points.length; i++) result += points[i].get_point();
console.log(result);
