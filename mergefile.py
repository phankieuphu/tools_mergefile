import argparse
import os
import shutil


def replace_file(path, filename):
    source_path = 'D:\\Game\\MergeFile\\server1\\'+path
    target_path = 'D:\\Game\\MergeFile\\server2\\'+path
    source_file_path = os.path.join(
        source_path, filename)
    target_file_path = os.path.join(
        target_path, filename)
    os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

    if os.path.exists(source_file_path):
        shutil.copy2(source_file_path, target_file_path)
        print(f"Replaced {filename} from {source_path} to {target_path}")
    else:
        print(f"{filename} not found in {source_path}")


def main():

    # remove file
    if os.path.exists("filename.txt"):
        os.remove("filename.txt")
    else:
        print("filename.txt does not exist")
    if os.path.exists("filepath.txt"):
        os.remove("filepath.txt")
        print("filepath.txt deleted")
    else:
        print("filepath.txt does not exist")

    with open('fullfile.txt', 'r') as file:
        listFullFile = [line.strip() for line in file]
    for j in listFullFile:
        parts = j.split("/")
        filename = parts[-1]
        pahts = "/".join(parts[:-1])
        print("File pahts", pahts)
        f = open('filename.txt', 'a')
        p = open('filepath.txt', 'a')
        p.write(pahts)
        p.write('\n')
        f.write(filename)
        f.write('\n')

    with open('filename.txt', 'r') as file:
        list_file_update = [line.strip() for line in file]
    with open('filepath.txt', 'r') as file:
        list_path = [line.strip() for line in file]
    for i in range(len(list_path)):
        replace_file(list_path[i], list_file_update[i])


if __name__ == "__main__":
    main()
