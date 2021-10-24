// Implement a function that takes two numbers, testVariable1 and testVariable2 and returns their greatest common divisor.

function gcd(testVariable1, testVariable2) {
  if (testVariable1 === testVariable2) return testVariable1;

  if (testVariable1 > testVariable2) {
    return gcd(testVariable1 - testVariable2, testVariable2);
  } else {
    return gcd(testVariable1, testVariable2 - testVariable1);
  }
}

// This solution relies on a mathematical simplification.
// If m > n then gcd(m, n) is the same as gcd(m-n, m). This is because if m/d and n/d both leave no remainder then (m-n)/d leaves no
// remainder
X;
