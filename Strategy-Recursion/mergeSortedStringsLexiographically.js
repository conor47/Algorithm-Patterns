function merge(string1, string2) {
  let newString = '';
  if (string1.length === 0) {
    if (string2.length === 0) {
      return '';
    }
  } else if (string1.length === 0) {
    return string2;
  } else if (string2.length === 0) {
    return string1;
  }

  if (string1[0] < string2[0]) {
    return newString + string1.substr(0, 1) + merge(string1.substr(1), string2);
  } else {
    return newString + string2.substr(0, 1) + merge(string1, string2.substr(1));
  }
}

console.log(merge('Uac', 'bst'));
