# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    arr = []
    i = 0
    j = 0
    # Sort until one array is done
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            arr.append(arrA[i])
            i += 1
        else:
            arr.append(arrB[j])
            j += 1
    # The other list might still have elements, so append them after
    while i < len(arrA):
        arr.append(arrA[i])
        i += 1
    while j < len(arrB):
        arr.append(arrB[j])
        j += 1

    # for i in range(0, len(merged_arr)):
    #     if not arrA or arrA[0] > arrB[0]:
    #         merged_arr[i] = arrB.pop(0)
    #     elif not arrB or arrB[0] > arrA[0]:
    #         merged_arr[i] = arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # break the array down recursively
    # base case: when the lists get down to lengths of 1

    # if len(arr) < 2:
    #     return arr

    # mid = len(arr) // 2
    # left = merge_sort(arr[:mid])
    # right = merge_sort(arr[mid:])

    # arr = merge(left, right)

    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    #         print(arr)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    i = start
    j = mid + 1
    # Loop until a region is done
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            i += 1
        else:
            # Organize elements to current spot
            j_index, j_value = j, arr[j]
            while j_index > i:
                arr[j_index] = arr[j_index-1]
                j_index -= 1
            arr[i] = j_value
            i += 1
            j += 1
            mid += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (r - l) < 1:
        return arr
    # Get middle index, split array, and recursively run sort again
    m = (l + r) // 2
    arr = merge_sort_in_place(arr, l, m)
    arr = merge_sort_in_place(arr, m+1, r)
    # Merge two eventually-sorted arrays together
    arr = merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
