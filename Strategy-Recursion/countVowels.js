// given a string return the number of vowels in the string

function isVowel(char) {
  let vowels = 'aeiou';
  char = char.toLowerCase();

  if (vowels.indexOf(char) !== -1) return true;
  else return false;
}

function vowelsCount(str, strLength) {
  if (strLength === 1) {
    return Number(isVowel(str[0]));
  }

  return vowelsCount(str, strLength - 1) + isVowel(str[strLength - 1]);
}

let test = 'conor';
console.log(vowelsCount(test, 4));
