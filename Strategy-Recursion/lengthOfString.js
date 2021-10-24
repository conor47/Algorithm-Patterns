// write a recursive function which given a string returns its length

function stringLength(string) {
  if (string.length === 0) return 0;

  return 1 + stringLength(string.substr(1));
}

console.log(stringLength('conorladrigan'));
