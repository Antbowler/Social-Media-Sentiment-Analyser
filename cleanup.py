import sys
import os.path


def main():
    if(len(sys.argv) != 2):
        print("Usage: python cleanup.py {filename}.txt")
        return
    
    fname = sys.argv[1]
    if(not os.path.isfile(fname)):
        print(f"Err: file {fname} doesn't exist")
        return
    
    file = open(fname, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    cleaned = list(dict.fromkeys(lines))

    cleaned_file = open(fname, "w", encoding="utf-8")
    for line in cleaned:
        cleaned_file.write(f"{line}\n")

    cleaned_file.close()

    
if __name__ == "__main__":
    main()