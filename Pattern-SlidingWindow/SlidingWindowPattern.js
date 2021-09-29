// Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

// The brute force solution

function averages_of_subarrays(k, arr) {
  const result = [];

  for (let i = 0; i < arr.length; i++) {
    sum = 0.0;

    for (let j = 0; j < i + k; j++) {
      sum += arr[j];
    }
    result.push(sum / K);
  }

  return result;
}

//

function averages_of_subarrays_efficient(k, arr) {
  const result = [];
  let windowSum = 0.0;
  let windowStart = 0;

  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    windowSum += arr[windowEnd];

    // slide the window. We so not slide unless we have hit the required window of size k
    if (windowEnd >= k - 1) {
      result.push(windowSum / k);
      windowSum -= arr[windowStart];
      windowStart += 1;
    }
  }
  return result;
}
