import os
import sys
"""
Simple deduplication of two benchmark folder by comparing file name.
Further complex deduplication with file content comparison is not implemented.
"""
def get_file_list(dir_path, file_extension=".sol"):
    file_list = []
    file_dict = {}
    for root, dirs, files in os.walk(dir_path):
        files.sort()
        for name in files:
            if name.endswith(file_extension):
                file_dict[name] = os.path.join(root, name)
    return file_dict
def get_full_path(dir_path, file_list):
    full_path_list = []
    for file_name in file_list:
        full_path_list.append(os.path.join(dir_path, file_name))
    return full_path_list
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python analyze_file_names.py <folder1> <folder2>")
        sys.exit(1)
    print ("Folder 1: {}".format(sys.argv[1]))
    print ("Folder 2: {}".format(sys.argv[2]))
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    file_dict1 = get_file_list(path1)
    file_dict2 = get_file_list(path2)
    file_list1 = list(file_dict1.keys())
    file_list2 = list(file_dict2.keys())
    print("Files in folder 1: {}".format(len(file_list1)))
    print("Files in folder 2: {}".format(len(file_list2)))
    print("Files in both folders: {}".format(len(set(file_list1).intersection(file_list2))))
    print("Files in folder 1 but not in folder 2: {}".format(len(set(file_list1).difference(file_list2))))
    print("Files in folder 2 but not in folder 1: {}".format(len(set(file_list2).difference(file_list1))))
    print("file_list folder 1 but not in folder 2")
    file_names = set(file_list1).difference(file_list2)
    diff_file_list1 = [file_dict1[item] for item in file_names]
    [print(item) for item in sorted(diff_file_list1)]

