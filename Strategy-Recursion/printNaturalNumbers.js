// print natural numbers within a given range using direct recursion

function printNatural(lowerBound, upperBound) {
  if (lowerBound > upperBound) {
    return;
  }

  console.log(lowerBound);
  printNatural(lowerBound + 1, upperBound);
}

// print the natural numbers within a given range using indirect recursion

function printNaturalIndirect(lowerBound, upperBound) {
  if (lowerBound <= upperBound) {
    console.log(lowerBound);
    lowerBound += 1;
    helperFunction(lowerBound, upperBound);
  }
}

function helperFunction(lowerBound, upperBound) {
  if (lowerBound <= upperBound) {
    console.log(lowerBound);
    lowerBound += 1;
    printNaturalIndirect(lowerBound, upperBound);
  }
}

printNaturalIndirect(1, 100);
