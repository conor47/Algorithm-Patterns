// Write a function that takes a variable testVariable, which contains a string, and checks whether or not it is a palindrome.

function palindrome(string) {
  if (string.length <= 1) return true;

  if (string[0] === string[string.length - 1]) {
    return palindrome(string.substr(1, string.length - 2));
  }
  return false;
}

console.log(palindrome('madamm'));
