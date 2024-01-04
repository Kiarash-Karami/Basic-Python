def binary_search(list, target):
    """
    Perform binary search on a sorted list to find the index of the target element.

    Parameters:
    - list: The sorted list to search.
    - target: The element to search for.

    Returns:
    - int: Index of the target element if found, -1 otherwise.
    """
    Low = 0
    high = len(list) - 1

    while Low <= high:
        mid = (Low + high) // 2
        mid_element = list[mid]

        if mid_element == target:
            return mid # Target found, return its index.
        elif mid_element < target:
            Low = mid + 1
        else:
            high = mid - 1
    
    return -1 # Target not found in the list.

# Example usage:
example_list = [8,4,5,6,3,4,7,8,9,10,4]
target_element = 7

result = binary_search(example_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")