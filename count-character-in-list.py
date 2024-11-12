def count_character_in_list(strings, char):

    count = 0

    # Loop through each string in the list
    for i in strings:
        # Loop through each character in the current string
        for j in i:
            # If the character matches char, increment the counter
            if j == char:
                count += 1

    return count
