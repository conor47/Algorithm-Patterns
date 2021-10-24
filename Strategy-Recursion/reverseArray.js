// write a recursive function that reverses a given array

function reverse(arr) {
  if (arr.length === 0) return [];

  return arr.slice(-1).concat(reverse(arr.slice(0, -1)));
}

console.log(reverse([1]));
