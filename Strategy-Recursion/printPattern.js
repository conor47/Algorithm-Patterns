// function which takes a target number and another number and prints pattern

function printPattern(target, decrement) {
  if (target <= 0) {
    console.log(target);
    return;
  }
  console.log(target);

  printPattern(target - decrement, decrement);

  console.log(target);
}

printPattern(100, 10);
