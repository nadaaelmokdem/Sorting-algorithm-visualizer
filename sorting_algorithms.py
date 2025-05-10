def quick_sort(arr): 
    """
    Sorts an array using the Quick Sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return _merge(left, right)

def _merge(left, right):
    """
    Helper function for Merge Sort. Merges two sorted arrays into a single sorted array.
    """
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
if __name__ == '__main__':
    # Example usage:
    test_array = [5, 2, 8, 1, 9, 4, 7, 3, 6]

    print("Original array:", test_array)

    sorted_quick_sort = quick_sort(test_array.copy())  # Use copy() to avoid modifying the original
    print("Quick Sort:", sorted_quick_sort)

    sorted_merge_sort = merge_sort(test_array.copy())
    print("Merge Sort:", sorted_merge_sort)

    sorted_insertion_sort = insertion_sort(test_array.copy())
    print("Insertion Sort:", sorted_insertion_sort)
