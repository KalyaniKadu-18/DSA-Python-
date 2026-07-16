# Function to perform Binary Search
def binary_search(arr, target):
    left = 0                    # Starting index
    right = len(arr) - 1        # Ending index

    # Loop until left index crosses right index
    while left <= right:
        mid = (left + right) // 2   # Find middle index

        # If target is found at mid
        if arr[mid] == target:
            return mid              # Return index where element is found

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    return -1                        # Element not found


# Binary search works only on sorted array
arr = [10, 20, 30, 40, 50]
target = 60

# Call the function
result = binary_search(arr, target)

# Print the result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
