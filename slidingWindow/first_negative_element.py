# Problem Definition:
# Given an array of integers, find the first negative integer in every window (subarray) of size k.
# If a window does not contain a negative integer, append 0 to the result list for that window.

# Initialize the array and parameters for the sliding window
array = [1, -4, -5, 9, -7, 8]
i = 0  # Start of the window
j = 0  # End of the window
negative_indices = []  # List to store indices of negative numbers within the window
first_negatives = []  # List to store the first negative in each window
k = 3  # Size of the window

# Iterate through the array using a sliding window approach
while j < len(array):
    # Append the index of the current element if it's negative
    if array[j] < 0:
        negative_indices.append(j)
    
    # Check if the window has reached the desired size
    if j - i + 1 < k:
        j += 1  # Expand the window by moving the end pointer
    elif j - i + 1 == k:
        # Check if there are any negative indices within the current window
        if negative_indices:
            # Ensure the oldest negative index is within the window's range
            if negative_indices[0] >= i:
                first_negatives.append(array[negative_indices[0]])
            else:
                first_negatives.append(0)  # No negative number in the current window
            
            # Remove the index if it's at the start of the current window
            if negative_indices[0] == i:
                negative_indices.pop(0)
        else:
            first_negatives.append(0)  # Append 0 if no negative numbers are in the current window

        # Move the window forward
        i += 1
        j += 1

# Output the results
print(first_negatives)
