import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    # Store input data (name and hash) in an OrderedDict
    input_data = OrderedDict()
    # Dictionary to store hashed passwords and corresponding numbers
    password_dict = OrderedDict()

    # Read input file and populate input_data
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            input_data[row[0]] = row[1]

    # Generate hashed passwords and store them in password_dict
    for num in range(1000, 9999):
        hsh = hashlib.sha256(str(num).encode()).hexdigest()
        password_dict[hsh] = num

    # Write cracked passwords to the output file
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for name, hash_value in input_data.items():
            # Check if the hashed password exists in the dictionary
            if str(hash_value) in password_dict:
                # Write the name and corresponding cracked password to the output file
                writer.writerow([name, password_dict[str(hash_value)]])