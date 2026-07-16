# Function to perform Linear Search
def linear_Search(array, target):
    # Loop through each index of the array
    for i in range(len(array)):
        # Check if the current element matches the target
        if array[i] == target:
            return i          # Return index if element is found
    return -1                 # Return -1 if element is not found


# Define the array
array = [10, 20, 30, 50, 40]

# Define the target element to search
target = 30

# Call the linear search function
result = linear_Search(array, target)

# Check the result and print output
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
