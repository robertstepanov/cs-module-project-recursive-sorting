# Divide and conquer 

# 1. find a pivot - use the midpoint or pick the first or last element in array
# 2. partition all the data around the pivot
# runtime O(n log n) is the best possible runtime for general purpose sorting algorithms

# when writing a recursive algorithm
#1. what's our base case/terminatin case?
#2. if we aren't in the base case, how are we moving towards it

def partition(data):
    # pick the first element in data as our pivot
    pivot = data[0]
    left = []
    right = []

    for x in data[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, pivot, right

def quicksort(data):
    # base case
    if len(data) == 0:
        return data 

    # partition handles picking the pivot element
    # # and paritioning the data around the pivot
    # # left is the left sub-list
    # # right is the right sub-list    

    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)

    