# Takes a directory of contracts and compares the `naive_checksum.txt` file for each contract to identify duplicates
#
# Usage: Python find-duplicates.py <directory> <output_json_file>


import os
import argparse
from collections import defaultdict
import json

empty_checksum = "d41d8cd98f00b204e9800998ecf8427e"

def find_duplicates(directory, output_file):
    checksum_dict = defaultdict(list)
    for foldername in os.listdir(directory):
        contract_path = os.path.join(directory, foldername)
        if os.path.isdir(contract_path):
            checksum_file = os.path.join(contract_path, "naive_checksum.txt")
            if os.path.exists(checksum_file):
                with open(checksum_file, 'r') as file:
                    checksum = file.read()
                if checksum == empty_checksum:
                    continue
                checksum_dict[checksum].append(foldername)

    keys = checksum_dict.keys()
    for checksum in list(keys):
        paths = checksum_dict[checksum]
        if len(paths) > 1:
            print(f"{checksum}:")
            for path in paths:
                print(f"- {path}")
        else:
            del checksum_dict[checksum]

    with open(output_file, 'w') as f:
        json.dump(checksum_dict, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find duplicate checksums.')
    parser.add_argument('dir', type=str, help='The directory to process')
    parser.add_argument('output', type=str, help='The directory to process')

    args = parser.parse_args()
    find_duplicates(args.dir, args.output)
