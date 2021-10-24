// Implement a function that takes a number testVariable and returns that row of the Pascal’s triangle.

function printPascal(testVariable) {
  let line = [1];
  if (testVariable === 0) return [1];
  else {
    let previousLine = printPascal(testVariable - 1);

    for (let i = 0; i < previousLine.length - 1; i++) {
      line.push(previousLine[i] + previousLine[i + 1]);
    }
    line.push(1);
  }
  return line;
}

console.log(printPascal(2));
