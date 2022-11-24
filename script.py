import os
import glob
import sys

if len(sys.argv) == 4:
    os.chdir(sys.argv[1])
    for file in glob.glob(sys.argv[2]):
        file_name = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]
        new_file_name = file_name[:-int(sys.argv[3])] + extension
        try:
            os.rename(file, new_file_name)
        except OSError as e:
            print(e)
        else:
            print(f"Renamed {file} to {new_file_name}")
else:
    print("\nScript should be used like below:\n")
    print("     python script.py DIR PATTERN SLICE_LEN\n")
    print("DIR       - path to directory")
    print("PATTERN   - pattern for files, for example '*.json'")
    print("SLICE_LEN - number of symbols to remove from file name ")