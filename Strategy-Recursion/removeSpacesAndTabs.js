// write a function which given a string returns a the string with all spaces and tabs removed

function remove(string) {
  if (string.length === 0) return string;

  if (string[0] === '\t' || string[0] === ' ') {
    return remove(string.substr(1));
  } else {
    return string[0] + remove(string.substr(1));
  }
}

console.log(remove('hello world my nameis '));
