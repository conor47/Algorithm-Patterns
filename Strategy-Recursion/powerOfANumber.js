// write a recursive function which raises some given number to a given exponent

function power(base, exponent) {
  if (exponent === 0) return 1;

  return base * power(base, exponent - 1);
}

console.log(power(10, 6));
