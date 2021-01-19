# Python practice implementing insertion sort
# Based on pseudocode from "Introduction to Alorithms" by Cormen - Section 2.1

import random

# takes a list of integers A, sorts it
def insertionSort(A):
    for j in range(1, len(A)):          # loop for all items, last item sorted automatically
        key = A[j]                      # the current item to sort
        i = j - 1                       # start comparisons before current index
        while i >= 0 and A[i] > key:    # check all the previous items
            A[i + 1] = A[i]             # bump this item back to make room
            i = i - 1                   # decrement i
        A[i + 1] = key                  # assign the current item to the correct place
    return A

# reproduce the same results by passing and int, otherwise pass None
random.seed()

# this gives ten pseudo-random numbers between 1 and 100
A = [random.randrange(1,100,1) for i in range(10)]
print(f'List of ten random numbers is {A}')
A_prime = insertionSort(A)
print(f'Sorted list is {A_prime}')