import csv
import os
import sys

"""
Validate the new labels csv files in SolidiFI++ with labels from MI_ISSTA unified dataset.
Run python validate_unified_dataset.py <path_to_SolidiFI++_dataset>
"""
reference_result = {
    "buggy_1.sol": [82, 99, 114, 219, 235],
    "buggy_3.sol": [29, 40, 70, 230, 286, 301],
    "buggy_4.sol": [34, 117, 180, 194, 260],
    "buggy_9.sol": [60, 101, 109, 142, 184, 336, 423, 442],
    "buggy_11.sol": [43, 51, 81, 145, 202, 241, 338, 415, 433],
    "buggy_16.sol": [72, 98, 116, 140, 294, 319, 341, 386, 526, 577],
    "buggy_23.sol": [145, 197, 393, 486, 494, 511, 528, 579],
    "buggy_26.sol": [77, 85, 115, 149, 246, 300, 317],
    "buggy_29.sol": [185, 309, 381, 447, 464],
    "buggy_33.sol": [22, 144, 152, 183, 201, 268, 314, 330],
    "buggy_36.sol": [86, 108, 116, 146, 272, 299, 318, 329, 356, 653, 667],
    "buggy_37.sol": [71, 97, 105, 135, 206, 273, 301, 397, 474, 492],
    "buggy_39.sol": [30, 79, 89, 116],
    "buggy_41.sol": [100, 175, 269, 297],
    "buggy_45.sol": [38, 49, 77, 102, 140, 159, 167, 232, 380],
    "buggy_48.sol": [53, 71, 79, 136, 151, 170, 240, 376, 460, 478],
}
total_bugs = 0
def validate_file(ref, file_index, path):
    global total_bugs
    annotation_file = os.path.join(path, f"BugLog_{file_index}.csv")
    # Read the injected bug logs
    print (annotation_file)
    bug_annots = []
    with open(annotation_file, "r") as f:
        reader = csv.reader(f)
        bug_log_list = list(reader)
        bug_log_list = bug_log_list[1 : len(bug_log_list)]
        bug_log_list.sort(key=lambda a: int(a[0]))
        # print (bug_log_list, len(bug_log_list))
        # print (ref, len(ref))
        assert(len(bug_log_list) == len(ref))
        total_bugs += len(ref)
        for idx, ibug in enumerate(bug_log_list):
            bug_name = ibug[2].strip()
            start_line = int(ibug[0])
            end_line = start_line + int(ibug[1])
            # print (bug_name, start_line, end_line)
            # print (ref[idx])
            assert(bug_name == "Reentrancy" or bug_name == "Re-entrancy")
            assert(ref[idx] >= start_line and ref[idx] <= end_line)
    return True
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate_unified_dataset.py <path_to_SolidiFI++_dataset>")
        sys.exit(1)
    print ("Path to SolidiFI++ dataset: {}".format(sys.argv[1]))
    print ("Path to Reentrancy folder : {}".format(os.path.join(sys.argv[1], "Re-entrancy")))
    path = os.path.join(sys.argv[1], "Re-entrancy")
    file_list = os.listdir(path)
    file_list = [f for f in file_list if f.endswith(".csv")]
    file_list.sort()
    for file_name in file_list:
        file_index = int("".join(filter(str.isdigit, file_name)))
        ref_key = f"buggy_{file_index}.sol"
        if not validate_file(reference_result[ref_key], file_index, path):
            print(f"Error in file {file_name}")
            sys.exit(1)
    print("All files are validated successfully, total {} bugs".format(total_bugs))
