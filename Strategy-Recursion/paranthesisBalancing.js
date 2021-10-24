// Implement a function that takes an array testVariable containing opening ( and closing parenthesis ) and determines whether or not the brackets in the array are balanced. The function also takes startIndex = 0 and currentIndex = 0 as parameters.

function balanced(arr, startIndex = 0, currentIndex = 0) {
  if (startIndex === arr.length) {
    return currentIndex === 0;
  }

  if (currentIndex < 0) {
    return false;
  }

  if (arr[startIndex] === '(') {
    return balanced(arr, startIndex + 1, currentIndex + 1);
  } else if (arr[startIndex] === ')') {
    return balanced(arr, startIndex + 1, currentIndex - 1);
  } else return false;
}

console.log(balanced(['(', ')', '(', ')', '(', ')']));
