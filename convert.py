#!/usr/bin/env python3

# pip install markdown
# or
# sudo apt install python3-markdown
import markdown
from os import listdir
from os.path import isfile, join
from sys import argv


def get_file_list(mypath):
# Get the list of all files ending with .md in the given mypath
    files = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and str(f).endswith(".md"))]
    return(files)

def get_file_contents(filename):
# Returns the contents of a file by given filename in a string
    with open(filename) as f: contents = f.read()
    return(contents)

def set_file_contents(filename, content):
# Fill a given file by given filename with the given content string
    with open(filename, "w") as text_file:
        text_file.write(content)

if len(argv) != 2:
    print("Usage: convert.py filename|all")
    print("all means all files ending with .md in the current directory")
    exit(1)  # invalid usage

param = argv[1]
if argv[1] == "all":     # all means all files ending with .md
    files = get_file_list(".")
else:
    if not isfile(param):    # Check if the argument is a valid file
        print("File : ", param, "is not found")
        exit(2)  # invalid filename
    else:
        files = []
        files.append(param)   # Append given argument to the files list
    
# Get the contents of html_header, html_footer and md_header

html_header = get_file_contents("htmlheader.txt")
html_footer = get_file_contents("htmlfooter.txt")
md_header = get_file_contents("mdheader.txt")
for file in files:
    # Set the name of the output file
    output_file = file[:-2] + "html"
    contents = md_header + get_file_contents(file) 
    html = html_header + markdown.markdown(contents, extensions=['extra']) + html_footer
    set_file_contents(output_file, html)
    print(file, "converted to html as", output_file)
exit(0)

