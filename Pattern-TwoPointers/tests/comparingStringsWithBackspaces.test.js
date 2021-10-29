const compare = require('../comparingStringsWithBackspaces');

test('compares equal strings successfully', () => {
  expect(compare('abcc##', 'abc#')).toBe(true);
});

test('compares unequal strings successfully', () => {
  expect(compare('abcc#', 'abc#')).toBe(false);
});
