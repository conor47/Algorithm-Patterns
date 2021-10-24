// write a recursive function which takes an array and a key as arguements and returns the number of times the key appears in the array

function occurences(arr, key) {
  if (arr.length === 0) return 0;

  if (arr[0] === key) {
    return 1 + occurences(arr.slice(1), key);
  } else {
    return 0 + occurences(arr.slice(1), key);
  }
}

console.log(occurences([1, 2, 3, 3, 4], 3));
