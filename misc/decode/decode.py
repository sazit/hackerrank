def read_file_to_2d_array(file_path):
    # Initialize an empty list to store the 2D array
    text_file_2d = []
    
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip newline characters and split the line by space
            parts = line.strip().split(' ')
            # Convert the first part to integer and keep the second part as is
            entry = [int(parts[0]), parts[1]]
            # Append the entry to the 2D array
            text_file_2d.append(entry)
        
        text_file_2d_sorted = sorted(text_file_2d, key=lambda x: x[0])
    
    # Return the 2D array
    return text_file_2d_sorted

def output_specific_elements(arr):
    # Initialize variables
    output_elements = []
    index = 0  # This will track the current index to be accessed
    step = 2   # This will track the current step size
    
    # Loop until the index exceeds the length of the array
    while index < len(arr):
        # Append the current element to the output list
        output_elements.append(arr[index])
        # Update the index for the next element based on the step
        index += step
        # Increase the step size for the next iteration
        step += 1
    
    return output_elements

def print_central_aligned_pyramid(arr):
    # Extract just the words (second item of each sub-list) from the sorted array
    words = [item[1] for item in arr]

    # Determine the total number of lines in the pyramid
    total_lines = 1
    while (total_lines * (total_lines + 1)) // 2 <= len(words):
        total_lines += 1
    total_lines -= 1  # Adjust because the loop exits one step beyond

    # Calculate the maximum width of the pyramid for central alignment
    # Assuming the longest line is the last line and includes spaces between words
    if total_lines > 0:
        max_width = len(' '.join(words[:total_lines]))

    # Print each line of the pyramid
    word_index = 0
    for line in range(1, total_lines + 1):
        line_words = ' '.join(words[word_index:word_index + line])
        print(line_words.center(max_width))
        word_index += line


# Example usage:
# file_path = 'textfile.txt'
file_path = input("Enter the file name or path: ")

text_file_2d_array = read_file_to_2d_array(file_path)
# print(text_file_2d_array)

# Accessing elements, for example, text_file_2d_array[0][0] and text_file_2d_array[0][1]
# print(text_file_2d_array[0][0], text_file_2d_array[0][1])

print_central_aligned_pyramid(text_file_2d_array)

# print(output_specific_elements(text_file_2d_array))
print([item[1] for item in output_specific_elements(text_file_2d_array)])


