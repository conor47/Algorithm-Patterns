// An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

// You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

// To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

// Return the modified image after performing the flood fill.

// Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
// Output: [[2,2,2],[2,2,0],[2,0,1]]
// Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
// Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

let floodFill = function (image, sr, sc, newColor) {
  if (image[sr][sc] === newColor) return image;
  fill(image, image[sr][sc], sr, sc, newColor);
  return image;
};

let fill = function (image, color, sr, sc, newColor) {
  if (
    sr < 0 ||
    sr >= image.length ||
    sc < 0 ||
    sc >= image[0].length ||
    image[sr][sc] !== color
  ) {
    return;
  }
  image[sr][sc] = newColor;
  fill(image, color, sr + 1, sc, newColor);
  fill(image, color, sr - 1, sc, newColor);
  fill(image, color, sr, sc + 1, newColor);
  fill(image, color, sr, sc - 1, newColor);
};

// time complexity is O(N * M)

// Space complexity is
