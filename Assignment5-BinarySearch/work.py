import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    lines = 0
    p = 1
    while v // p > 0:
        lines += v // p
        p *= k
    return lines

# Input: n an integer representing  the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    v = 1
    while sum_series(v, k) < n:
        v += 1

    return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    lower = 1
    upper = n
    its = 0
    while lower < upper and its < 100:
        v_mid = (upper+lower) // 2
        if sum_series(v_mid, k) >= n:
            upper = v_mid
        else:
            lower = v_mid + 1
        its += 1
    
    return lower

def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for i in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        n = int(inp[0])
        k = int(inp[1])
        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))
        temp = i
        i = temp
        print()
        print()

if __name__ == "__main__":
  main()
