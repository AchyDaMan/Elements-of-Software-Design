"""
  File: intervals.py
  Description: find and merge intervals

  Student Name: Achintya Yedavalli
  Student UT EID: asy397

  Partner Name: I have a coding buddy but we didn't work on this together

  Course Name: CS 313E
  Unique Number: 50165
  Date Created: 9/9/24
  Date Last Modified: 9/10/24
"""
import sys

def merge_tuples (tuples_list):
    """
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
    """
    #Merge the tuples
    tuples_list.sort()
    i = 1
    while i < len(tuples_list):
        # if the upper boundary of the left interval is bigger than the left boundary of the
        # right interval, they overlap
        if tuples_list[i-1][1] >= tuples_list[i][0]:
            # find which one is the smallest
            minimum = min(tuples_list[i-1][0], tuples_list[i][0])
            maximum = max(tuples_list[i-1][1], tuples_list[i][1])
            # add merged tuple to i-1, pop out i to get new i
            tuples_list[i-1] = tuple((minimum, maximum))
            tuples_list.pop(i)
        # the loop will repeat unless it can't be merged, then a new interval is chosen
        else:
            i += 1

    return tuples_list

def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    interval_sizes = []

    for tup in tuples_list:
        interval_sizes.append(tup[1]-tup[0])

    sorted_intervals = [tupl for _, tupl in sorted(zip(interval_sizes, tuples_list))]
    return sorted_intervals


# main function
def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    sys.stdout.write(f'{merged}\n')
    sys.stdout.write(f'{sorted_merge}')

if __name__ == "__main__":
    main()
