// Given a set of distinct numbers, find all of its permutations.

// Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

//     {1, 2, 3}
//     {1, 3, 2}
//     {2, 1, 3}
//     {2, 3, 1}
//     {3, 1, 2}
//     {3, 2, 1}

// If a set has ‘n’ distinct elements it will have n!n!n! permutations.

const Deque = require('collections/deque');

const find_permutations = function (nums) {
  let result = [];
  let numsLength = nums.length;
  let permuatations = new Deque();
  permuatations.push([]);
  for (let i = 0; i < numsLength; i++) {
    let currentNum = nums[i];
    //   add current num to all existing permutations
    let n = permuatations.length;
    for (let p = 0; p < n; p++) {
      let oldPermutation = permuatations.shift();
      for (let j = 0; j < oldPermutation.length + 1; j++) {
        let newPermutation = oldPermutation.slice(0);
        newPermutation.splice(j, 0, currentNum);
        if (newPermutation.length === numsLength) {
          result.push(newPermutation);
        } else {
          permuatations.push(newPermutation);
        }
      }
    }
  }
  return result;
};

console.log(find_permutations([1, 3, 5]));
