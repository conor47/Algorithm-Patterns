// Implement a function that takes a variable testVariable, which contains a string of digits, and prints the sum of those digits

function sumOfDigits(string) {
  if (string.length === 0) return 0;

  return Number(string[0]) + sumOfDigits(string.substr(1));
}

console.log(sumOfDigits('4747'));
k;
