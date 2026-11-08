class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                matrix[top + i][right], matrix[bottom][right - i], matrix[bottom - i][left], matrix[top][left + i] = matrix[top][left + i], matrix[top + i][right], matrix[bottom][right - i], matrix[bottom - i][left]

            left += 1
            right -= 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna