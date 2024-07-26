import subprocess
import os


def get_files():
    find_command = "ls ~/Downloads"
    raw_input_allfiles = subprocess.getoutput(find_command)  # noqa: F821
    return raw_input_allfiles


def replace_white_space(raw_input_allfiles):
    raw_input_allfiles = raw_input_allfiles.replace(" ", "-")
    return raw_input_allfiles


def filter_pdfs(raw_input_allfiles):

    for line in raw_input_allfiles.split("\n"):
        if line.endswith(".pdf"):
            new_line = replace_white_space(line)
            os.system("rename ")
            os.system(f"mv ~/Downloads/{line} ~/Documents/pdfs")
            print(f"moved {line} to ~/Documents/pdfs\n")


def main():
    # raw_input_allfiles = get_files()
    # filter_pdfs(raw_input_allfiles)
    print(replace_white_space("h e ll o wo rld"))


if __name__ == "__main__":
    main()
