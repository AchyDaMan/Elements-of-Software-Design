"""
  File: spiral.py
  Description:

  Student Name: Achintya Yedavalli
  Student UT EID: asy397

  Partner Name: I have a coding buddy but we didn't work on this together

  Course Name: CS 313E
  Unique Number: 50165
  Date Created: 8/28/24
  Date Last Modified: 9/5/24

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")

 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""


def create_spiral(dim):
    spiral = [[0 for i in range(dim)] for j in range(dim)]

    i = dim//2
    j = dim//2

    steps = ['right_step', 'down_step', 'left_step', 'up_step']

    step_count = 1
    step_to_do = 0
    # for each number
    spiral[i][j] = 1
    number = 2
    while number < (dim*dim) + 1:
        # going throughn the step pattern
        for _ in range(step_count):
            if steps[step_to_do] == 'right_step':
                # a right step involves adding 1 to j
                j += 1
            elif steps[step_to_do] == 'down_step':
                # a down step involves adding 1 to i
                i += 1
            elif steps[step_to_do] == 'left_step':
                # a down step involves subtracting 1 from j
                j -= 1
            elif steps[step_to_do] == 'up_step':
                # am up step involves subtracting 1 from i
                i -= 1

            spiral[i][j] = number
            number += 1
            if number >= (dim * dim) + 1:
                break

        step_to_do += 1
        # reset it to beginning when done
        if step_to_do == 4:
            step_to_do = 0
        if steps[step_to_do] == 'left_step' or steps[step_to_do] == 'right_step':
            step_count += 1
    return spiral


def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    row, col = -1, -1
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == val:
                row, col = i, j
                break

    if row == -1 and col == -1:
        return 0

    # Calculate the sum of the numbers surrounding val
    total_sum = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                total_sum += grid[i][j]

    return total_sum - val


def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """
    # read the dimension of the grid and value from input file
    dim = int(input())
    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1
    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
