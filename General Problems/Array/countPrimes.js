// Given an integer n, return the number of prime numbers that are strictly less than n.

// Example 1:

// Input: n = 10
// Output: 4
// Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

// Example 2:

// Input: n = 0
// Output: 0

// Example 3:

// Input: n = 1
// Output: 0

// Constraints:

//     0 <= n <= 5 * 106

// Brute force solution. TLEs for large values of n

var countPrimes = function (n) {
  if (n <= 1) return 0;
  let count = 0;
  for (let i = 2; i < n; i++) {
    flag = true;
    for (let j = 2; j <= i; j++) {
      if (i % j === 0 && j !== 1 && j !== i) {
        flag = false;
        break;
      }
    }
    if (flag) {
      count += 1;
    }
  }
  return count;
};

// Time complexity is O(n^2)

// Space complexity is O(1)

// Sieve of Eratosthenses solution

var countPrimes = function (n) {
  let primes = Array(n).fill(true);

  for (let i = 2; i * i < primes.length; i++) {
    if (primes[i]) {
      for (let j = i; j * i < primes.length; j++) {
        primes[j * i] = false;
      }
    }
  }
  let count = 0;
  for (let i = 2; i < primes.length; i++) {
    if (primes[i]) {
      count += 1;
    }
  }
  return count;
};
