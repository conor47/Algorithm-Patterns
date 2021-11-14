//  write a function which takes a string an generates all permutations of that string

const permute = (letters) => {
  let result = [];
  dfsRecursive(letters, [], Array(letters.length).fill(false), result);
  return result;
};

const dfsRecursive = (letters, path, used, res) => {
  // if our path is the same length as our array or letters we have generated a valid permutation given our constraints
  if (path.length === letters.length) {
    // we make a copy of the path array otherwise we would push in a reference to the same array each time
    res.push(Array.from(path));
    return;
  }

  for (let i = 0; i < letters.length; i++) {
    // skip used letters
    if (used[i]) continue;

    // add letter to permutation and mark as used
    path.push(letters[i]);
    used[i] = true;
    dfsRecursive(letters, path, used, res);
    // remove letter from permutation and mark as unused
    path.pop();
    used[i] = false;
  }
};

// space complexity is O(N)

console.log(permute('con'));
