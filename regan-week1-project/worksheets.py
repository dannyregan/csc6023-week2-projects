import random
import math

def generateArray():
    """
    Summary: Generates an array of 1000 randomly generated numbers between -100 and 100.

    Input: None

    Output: Returns the randomly generated array.
    """

    a = [math.floor((random.random() - 0.5) * 200) for num in range(1000)]
    return a


def MCSS():
    """
    Summary: Creates a randomized array of 1000 numbers between -100 and 100, then finds the maximum contiguous subsequence sum value.

    Input: None

    Output: The maximum contiguous subsequence sum value, and the starting and the ending indices of the subsequence.
    """

    a = generateArray()

    largest, acc = 0, 0                   # Used to find the largest subsequence
    start, end, current_start = 0, 0, 0   # Used to track the start and end indices

    for j in range(len(a)):
        acc += a[j]
        if (acc > largest):
            largest = acc
            start = current_start
            end = j
        elif (acc < 0):                   # The subsequence is reset
            current_start = j + 1         # Update the starting index
            acc = 0
    return largest, start, end

print(MCSS())