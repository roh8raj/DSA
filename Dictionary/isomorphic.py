def are_isomorphic(str1, str2):
    """
    Check if two strings are isomorphic.
    Two strings are isomorphic if the characters in one string can be replaced to get the second string.
    
    :param str1: First input string.
    :param str2: Second input string.
    :return: Boolean indicating whether the strings are isomorphic.
    """
    if len(str1) != len(str2):
        return False  # Strings of different lengths cannot be isomorphic

    # Create a mapping of each character from str1 to str2
    char_map = dict(zip(str1, str2))

    # Generate the transformed version of str1 using the mapping
    transformed_str1 = "".join(char_map[char] for char in str1)

    # Check if the transformed version of str1 matches str2
    if transformed_str1 == str2:
        return True
    else:
        return False

# Example strings
str1 = "foo"
str2 = "bar"

# Check if the strings are isomorphic and print the result
result = are_isomorphic(str1, str2)
print("The strings are isomorphic:" if result else "The strings are not isomorphic.")
