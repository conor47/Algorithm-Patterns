// write a recursive function which take an array and replaces all occurences of negative numbers with 0

function replaceNegative(arr) {
  if (arr.length === 0) return [];

  if (arr[0] < 0) {
    arr[0] = 0;
    return arr.slice(0, 1).concat(replaceNegative(arr.slice(1)));
  } else {
    return arr.slice(0, 1).concat(replaceNegative(arr.slice(1)));
  }
}

// alternative solution

function replace(arr, currentIndex) {
  if (currentIndex < arr.length) {
    if (arr[currentIndex] < 0) {
      arr[currentIndex] = 0;
    }
    replace(arr, currentIndex + 1);
  }
  return;
}

console.log(replaceNegative([1, 4, 6, -1, 3, -5]));
