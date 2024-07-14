input_file_path = "data/csv/E-commerse-customer-data.csv"
output_file_path = "data/csv/E-commerse-customer-data-modified.csv"

# Open the input file for reading
with open(input_file_path, "r") as input_file:

    # Open the output file for writing
    # with open(output_file_path, "w") as output_file:
    #
    #     # Read the header line and write it to the output FileExistsError

    with open(output_file_path, "w") as output_file:
        # Read the header line and write it to the output file
        header = input_file.readline().strip()
        output_file.write(header + "\n")

        # Initialize index
        index = 0

        # Iterate over each line in the input file
        for line in input_file:
            index += 1
            # Strip newline character and split the line into columns
            line = line.strip()
            columns = line.split(",")

            # Modify the second column (index 1)
            columns[0] = str(index)

            # Join columns back into a line
            modified_line = ",".join(columns)

            # Write the modified line to the output file
            output_file.write(modified_line + "\n")
