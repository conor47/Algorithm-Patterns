const slidingWindowPattern = require('../SlidingWindowPattern');

it('returns the correct answer given a valid input', () => {
  expect(slidingWindowPattern(3, [1, 2, 3, 4, 5])).toEqual([2, 3, 4]);
});

it('returns the incorrect answer given a valid input', () => {
  expect(slidingWindowPattern(3, [1, 2, 3, 4, 5])).not.toEqual([5, 6, 7]);
});
