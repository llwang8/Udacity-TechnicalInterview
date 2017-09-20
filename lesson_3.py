# Udacity Data Analyst Nanodegree

# Technical Interview

# Lesson 3. Searching and Sorting

# Quiz: Binary Search Practice
"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    n1 = 0
    n2 = len(input_array) - 1
    while n1 <= n2:
        n = (n2 + n1) / 2
        if value < input_array[n]:
            n2 = n - 1
        elif input_array[n] < value:
            n1 = n + 1
        else:
            return n

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

# Quiz: REcursion Practice
"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    return get_fib(position-1) + get_fib(position-1)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)

# iterative
def get_fib2(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    p = 2
    first, second = 0, 1
    next = first + second
    while p < position:
        p += 1
        first = second
        second = next
        next = first + second
    return next


"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    n = len(array)
    if n <= 1:
        return array
    else:
        p = n -1
        i = 0
        while i < p:
            if array[i] > array[p]:
                temp = array[i]
                array[i], array[p-1], array[p] = array[p-1], array[p], temp
                p -= 1
            else:
                i += 1
        return quicksort(array[0:p]) + quicksort(array[p:])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
