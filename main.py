from math import*

def all_scytale_solutions():    # Brute force solution for Scytale cipher by trying all offset-insertioncount combinations.
    input_string = input("Enter the encoded message here: ")
    for starting_offset in range(len(input_string)):    # Testing this particular starting offset before the first letter...
        for n_insertions in range(len(input_string)):   # Testing this particular number of insertions between meaningful letters...
            current_string = ""
            for ii in range(int(ceil((len(input_string) - starting_offset) / (n_insertions + 1)))):
                current_string = current_string + input_string[starting_offset + ii * (n_insertions + 1)]
            print(current_string)
        continue_flag = input("Move to the next offset and continue printing? (y/n): ")
        if continue_flag == "n":
            return


all_scytale_solutions()
