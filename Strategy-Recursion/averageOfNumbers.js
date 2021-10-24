// Implement a function that computes the average of all the numbers in an array.

function average(arr, currentIndex) {
  if (currentIndex === arr.length - 1) return arr[currentIndex];

  if (currentIndex === 0) {
    return (arr[currentIndex] + average(arr, currentIndex + 1)) / arr.length;
  }

  return arr[currentIndex] + average(arr, currentIndex + 1);
}

console.log(average([5, 10, 15, 20], 0));
