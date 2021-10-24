// implement the modulus operator recursively

function modulo(dividend, divisor) {
  if (dividend === 0) return 0;
  if (dividend < divisor) return dividend;

  return modulo(dividend - divisor, divisor);
}

console.log(modulo(12, 12));
