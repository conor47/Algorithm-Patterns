var addStrings = function (num1, num2) {
  let result = [];

  let carry = 0;
  let p1 = num1.length - 1;
  let p2 = num2.length - 1;

  while (p1 >= 0 || p2 >= 0) {
    let x1 = p1 >= 0 ? num1[p1] - '0' : 0;
    let x2 = p2 >= 0 ? num2[p2] - '0' : 0;
    let value = (x1 + x2 + carry) % 10;
    carry = Math.floor((x1 + x2 + carry) / 10);

    result.unshift(value);
    p1 -= 1;
    p2 -= 1;
  }

  if (carry) {
    result.unshift(carry);
  }

  return String(result.join(''));
};

// Time complexity is O(MAX(N1,N2)) where N1 and N2 are lengths the input strings

// Space complexity is O(max(N1,N2) since the new string is at most max(N1,N2) + 1

console.log(addStrings('456', '77'));
