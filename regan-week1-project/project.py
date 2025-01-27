import random
import math
import cProfile

# This sort function comes from my notes from CSC 6013 with Paulo Fernandes
def insertionSort(a):
    """
    Summary: Sorts an array.

    Input: An array of integers.

    Output: The sorted array of integers.
    """

    for i in range(len(a)-2, -1, -1):       # Start at the second to last element and move backwards each iteration. Stop before reaching -1
        for j in range(len(a)-1, i, -1):    # Start at the last element and move backwards each iteration. Stop before reaching i.
            if (a[i] > a[j]):
                a.insert(j, a.pop(i))       # Pop the element at index i from a and insert it at index j
                break
            
def main():
    """
    Summary: Generates a series of random arrays of numbers between 0 and 50,000 and sorts each. The first array is 1000 elements long and each array after that is 1000 elements longer than the last.

    Input: The number of arrays to be generated and sorted.

    Output: The cProfile of each sorted array.
    """

    def generateArrays(n):
        i = 1
        while i <= n:
            a = [math.floor((random.random()) * 50000) for num in range(1000 * i)]
            cProfile.runctx('insertionSort(a)', globals(), locals())
            i += 1

    generateArrays(10) 

main()