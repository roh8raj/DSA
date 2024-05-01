# Problem Definition:
# Given an array of integers, find the maximum sum of any contiguous subarray of size k.

# Array definition
array = [1, 2, 3, 4, 5, 6]
# Size of the subarray
k = 3

# Two pointer initialization
i = 0
j = 0
max_sum = 0  # Variable to store the maximum sum of any k-sized subarray
current_sum = 0  # Variable to store the current sum of the subarray

# Iterate through the array using a sliding window approach
while j < len(array):
    # Add the current element to the current sum
    current_sum += array[j]

    # Check if the window has not yet reached size k
    if j - i + 1 < k:
        j += 1
    # Once the window reaches size k
    elif j - i + 1 == k:
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)
        # Slide the window: subtract the element going out of the window and move the window forward
        current_sum -= array[i]
        i += 1
        j += 1

# Output the result
print(max_sum)
