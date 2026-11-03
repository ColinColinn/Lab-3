print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    # REQ-04: 0 numbers entered
    if n == 0:
        return 0

    # REQ-05: any value not an integer
    for value in arr_result:
        if not isinstance(value, int):
            return 2

    # REQ-03: 10 or more numbers entered
    if n >= 10:
        return 1

    # REQ-01 / REQ-02: fewer than 10 numbers, so sort
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            else:
                # Invalid sort order, so return an empty array
                arr_result = []

    return arr_result
