// For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

// Example 1:

// Input: N=2
// Output: (()), ()()

// Example 2:

// Input: N=3
// Output: ((())), (()()), (())(), ()(()), ()()()

const Dequeu = require('collections/deque');

class ParenthesesString {
  constructor(str, openCount, closeCount) {
    this.str = str;
    this.openCount = openCount;
    this.closeCount = closeCount;
  }
}

const generate_valid_parentheses = function (num) {
  result = [];
  let queue = new Dequeu();
  queue.push(new ParenthesesString('', 0, 0));
  while (queue.length > 0) {
    const ps = queue.shift();
    if (ps.openCount === num && ps.closeCount === num) {
      result.push(ps);
    } else {
      if (ps.openCount < num) {
        queue.push(
          new ParenthesesString(`${ps.str}()`, ps.openCount + 1, ps.closeCount)
        );
      }
      if (ps.openCount > ps.closeCount) {
        queue.push(
          new ParenthesesString(`${ps.str})`, ps.openCount, ps.closeCount + 1)
        );
      }
    }
  }

  return result;
};

console.log(
  `All combinations of balanced parentheses are: ${generate_valid_parentheses(
    2
  )}`
);
console.log(
  `All combinations of balanced parentheses are: ${generate_valid_parentheses(
    3
  )}`
);
