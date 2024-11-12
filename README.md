# Count Character in List of Strings

This Python function counts the occurrences of a specific character within a list of strings.

## Function: `count_character_in_list`

### Description
The `count_character_in_list` function iterates through each string in a given list and counts how many times a specified character appears across all the strings in the list.

### Parameters
- `strings` (list of str): A list of strings in which to count occurrences of the character.
- `char` (str): The character to count in each string.

### Returns
- `count` (int): The total number of times `char` appears in all strings in the list.

# Example:
strings = ["apple", "banana", "cherry"]
char = "a"
result = count_character_in_list(strings, char)
print(result)  # Output: 4
