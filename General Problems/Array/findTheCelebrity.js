// Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

// Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

// You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

// Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
// Output: -1
// Explanation: There is no celebrity.

// Constraints:

//     n == graph.length
//     n == graph[i].length
//     2 <= n <= 100
//     graph[i][j] is 0 or 1.
//     graph[i][i] == 1

const solution = function (knows) {
  /**
   * @param {integer} n Total people
   * @return {integer} The celebrity
   */
  return function (n) {
    let candidate = 0;
    let i = 1;
    while (i <= n - 1) {
      if (knows(candidate, i)) {
        candidate = i;
      }
      i += 1;
    }
    for (let i = 0; i <= n - 1; i++) {
      if ((i !== candidate && knows(candidate, i)) || !knows(i, candidate)) {
        return -1;
      }
    }
    return candidate;
  };
};

// Time complexity is O(N)

// Space complexity is O(1)

// Note this can be modelled as a graph problem
