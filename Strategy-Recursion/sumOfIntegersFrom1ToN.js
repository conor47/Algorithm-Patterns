// write a recursive function which returns the sum of the integers 1 through N

function sumToN(targetNumber) {
  if (targetNumber === 1) return 1;

  return targetNumber + sumToN(targetNumber - 1);
}

console.log(sumToN(6));
