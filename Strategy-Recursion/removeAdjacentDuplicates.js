// given a string remove all duplicate adjacent characters. Uppercase and lowercase are considered different chars

function removeDuplicates(string) {
  if (string.length === 0) return string;

  if (string[0] === string[1]) {
    return removeDuplicates(string.substr(1));
  } else {
    return string[0] + removeDuplicates(string.substr(1));
  }
}

console.log(removeDuplicates('hhellloWorrld'));
