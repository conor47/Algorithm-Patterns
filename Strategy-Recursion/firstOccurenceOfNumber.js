// Implement a function that takes an array arr, a testVariable containing the number to search and currentIndex containing the starting index as parameters and outputs the index of the first occurrence of testVariable in arr. If testVariable is not found in arr return −1-1−1.

// A variable arr that contains the array on which searching is to be performed.
// A variable testVariable that contains the number that needs to be searched.
// A variable currentIndex that contains the starting index of the arr array.

// We want to search for a targetNumber from index currentIndex to the end of the array.

function firstIndex(arr, testVariable, currentIndex) {
  if (currentIndex > arr.length) return -1;
  else if (arr[currentIndex] === testVariable) return currentIndex;

  return firstIndex(arr, testVariable, currentIndex + 1);
}

console.log(firstIndex([9, 8, 1, 7, 1, 7], 7, 0));
