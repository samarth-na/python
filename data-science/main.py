input_file_path = "data/csv/E-commerse-customer-data.csv"

output_file_path = "data/csv/E-commerse-customer-data-modified.csv"

# Open the input file for reading
with open(input_file_path, "r") as input_file:
    with open(output_file_path, "w") as output_file:
        header = input_file.readline().strip()

        _ = output_file.write(header + "\n")

        index = 0

        for line in input_file:
            index += 1
            line = line.strip()
            columns = line.split(",")

            # Modify the second column (index 1)
            columns[0] = str(index)

            modified_line = ",".join(columns)

            _ = output_file.write(modified_line + "\n")
