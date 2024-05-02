def count_character_occurrences(string):
    """
    Counts the occurrences of each character in the given string.
    
    :param string: The string to count character occurrences in.
    :return: A dictionary with characters as keys and their counts as values.
    """
    character_count = {}
    for character in string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

# The main string and the target string whose permutations we're counting in the main string.
main_string = "forxxorfxdofr"
target_string = "for"

# Get character count of the target string.
target_count = count_character_occurrences(target_string)

# Length of the target string, which will be the window size.
window_size = len(target_string)

# Initialize pointers for the sliding window and a counter for valid permutations.
i = 0
j = 0
valid_permutations_count = 0

# Start sliding window over the main_string.
while j < len(main_string):
    # Expand the window until it matches the size of the target string.
    if j - i + 1 < window_size:
        j += 1
    # When window size matches the target string size, check for match.
    elif j - i + 1 == window_size:
        # Extract the current substring.
        current_substring = main_string[i:j + 1]
        # Count characters in the current substring.
        current_count = count_character_occurrences(current_substring)
        
        # Compare dictionary counts to check if current substring is a permutation of the target string.
        if current_count == target_count:
            valid_permutations_count += 1
        
        # Move the window forward.
        i += 1
        j += 1

print("Count of permutations is", valid_permutations_count)
