import os
import sys
import json
def convert_to_smartian_format(input_file, output_file):
    final_res = []
    with open(input_file, 'r') as f :
        data = json.load(f)
        for key, val in data.items():
            final_res.append(f'{key},{val.get("name")},{val.get("compiler")}')
    with open(output_file, 'w') as f:
        f.write('\n'.join(final_res))
if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_to_smartian_format(input_file, output_file)