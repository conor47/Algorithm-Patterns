// You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

// Return the single element that appears only once.

// Your solution must run in O(log n) time and O(1) space.

// Example 1:

// Input: nums = [1,1,2,3,3,4,4,8,8]
// Output: 2

// Example 2:

// Input: nums = [3,3,7,7,10,11,11]
// Output: 10

// Constraints:

//     1 <= nums.length <= 105
//     0 <= nums[i] <= 105

// recursive binary search solution. Meets time complexity requirements but not space requirements

var singleNonDuplicate = function (nums) {
  return binarySearch(nums, 0, nums.length - 1);
};

const binarySearch = function (nums, start, end) {
  if (start > end) {
    return false;
  }

  let mid = Math.floor(start + (end - start) / 2);
  if (nums[mid - 1]) {
    if (nums[mid] === nums[mid - 1]) {
      return (
        binarySearch(nums, start, mid - 2) || binarySearch(nums, mid + 1, end)
      );
    }
  }
  if (nums[mid + 1]) {
    if (nums[mid] === nums[mid + 1]) {
      return (
        binarySearch(nums, start, mid - 1) || binarySearch(nums, mid + 2, end)
      );
    }
  }

  return nums[mid];
};

// Key observation is that the starting array must always have an odd number of elements.

var singleNonDuplicate = function (nums) {
  let low = 0;
  let high = nums.length - 1;

  while (low < high) {
    let mid = Math.floor(low + (high - low) / 2);
    let halves_even = (high - mid) % 2 === 0;
    if (nums[mid] === nums[mid + 1]) {
      if (halves_even) {
        low = mid + 2;
      } else {
        high = mid - 1;
      }
    } else if (nums[mid - 1] === nums[mid]) {
      if (halves_even) {
        high = mid - 2;
      } else {
        low = mid + 1;
      }
    } else {
      return nums[mid];
    }
  }
  return nums[low];
};

// Time complexity is O(Log N)

// Space complexity is O(1)
