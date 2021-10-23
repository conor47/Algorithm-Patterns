function reverseString(str) {
  if (str.length === 0) return str;
  else {
    return str[str.length - 1] + reverseString(str.substr(0, str.length - 1));
  }
}

let test = 'conor ladrigan';
console.log(reverseString(test));
