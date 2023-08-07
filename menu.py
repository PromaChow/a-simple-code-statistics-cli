#!/usr/bin/env python3

import argparse
import os
import pygount
import difflib
import filecmp
import subprocess
from termcolor import colored


def add(args):
    result = args.num1 + args.num2
    print(f"{args.num1} + {args.num2} = {result}")

def subtract(args):
    result = args.num1 - args.num2
    print(f"{args.num1} - {args.num2} = {result}")



def get_file_changes(commit1, commit2):
    command = ["git", "diff", commit1, commit2]
    output = subprocess.check_output(command, universal_newlines=True)

    changes_by_file = {}
    current_file = None
    current_changes = []

    for line in output.splitlines():
        if line.startswith("diff --git"):
            if current_file is not None:
                changes_by_file[current_file] = current_changes
            current_file = line.split()[-1]
            current_changes = []
        elif line.startswith(("+++", "---")):
            pass
        else:
            current_changes.append(line)

    if current_file is not None:
        changes_by_file[current_file] = current_changes

    return changes_by_file


def get_changed_files_count(args):

    command = ["git", "diff", "--numstat", args.folder1_path, args.folder2_path ]
    # command = ["git", "diff", "--numstat", args.folder1_path, args.folder2_path , "|", "wc", "-1"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    lines = stdout.decode('utf-8').strip().split('\n')
    changed_files_count = len(stdout.decode('utf-8').strip().split('\n'))

    print(colored("Folders Changed Summary:", "cyan"))
    print(colored("Added\tDeleted\tFile Path", attrs=["underline"]))

    for line in lines:
        added, deleted, path = line.split('\t')
        if added!='-' and deleted!='-':
            added = int(added) 
            deleted = int(deleted)

            added_colored = colored(str(added), "green")

            
            deleted_colored = colored(str(deleted), "red")

            print(f"{added_colored}\t{deleted_colored}\t{path}")

    # print("Standard Error:", stderr.decode("utf-8"))
    # output = subprocess.check_output(stderr=subprocess.STDOUT, universal_newlines=True)
    
    # changed_files_count = len(output.strip().split('\n'))
    # print(changed_files_count)
    # return changed_files_count








def compare_files(args):
    command = ["git", "diff", "--numstat", args.file1_path, args.file2_path ]
    # command = ["git", "diff", "--numstat", args.folder1_path, args.folder2_path , "|", "wc", "-1"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    lines = stdout.decode('utf-8').strip().split('\n')
    changed_files_count = len(stdout.decode('utf-8').strip().split('\n'))

    print(colored("Files Changed Summary:", "cyan"))
    print(colored("Added\tDeleted\tFile Path", attrs=["underline"]))

    for line in lines:
        added, deleted, path = line.split('\t')
        if added!='-' and deleted!='-':
            added = int(added) 
            deleted = int(deleted)

            added_colored = colored(str(added), "green")

            
            deleted_colored = colored(str(deleted), "red")

            print(f"{added_colored}\t{deleted_colored}\t{path}")
    

    command = ["git", "diff",  args.file1_path, args.file2_path ]
    # command = ["git", "diff", "--numstat", args.folder1_path, args.folder2_path , "|", "wc", "-1"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(colored('\n\n\nThe details\n',attrs=["underline"]))
    print(stdout.decode('utf-8'))


def sloc(args):
    command = ["cloc", args.path]
    # command = ["git", "diff", "--numstat", args.folder1_path, args.folder2_path , "|", "wc", "-1"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print( stdout.decode("utf-8"))
    

def main():
    parser = argparse.ArgumentParser(description="Simple command-line calculator tool.")
    subparsers = parser.add_subparsers(title="Operations", dest="operation")

    # Add sub-command for addition
    parser_sloc = subparsers.add_parser("sloc", help="Find the source lines of code of a file")
    parser_sloc.add_argument("path", type=str, help="file path")
    parser_sloc.set_defaults(func=sloc)



    parser_file = subparsers.add_parser("filediff", help="Find the source lines of code of a file")
    parser_file.add_argument("file1_path", type=str, help="file path")
    parser_file.add_argument("file2_path", type=str, help="file path")
    parser_file.set_defaults(func=compare_files)


    parser_file = subparsers.add_parser("folderdiff", help="Find the source lines of code of a file")
    parser_file.add_argument("folder1_path", type=str, help="file path")
    parser_file.add_argument("folder2_path", type=str, help="file path")
    parser_file.set_defaults(func=get_changed_files_count)
    
    

    # Add sub-command for subtraction
    parser_subtract = subparsers.add_parser("subtract", help="Subtract two numbers")
    parser_subtract.add_argument("num1", type=float, help="First number")
    parser_subtract.add_argument("num2", type=float, help="Second number")
    parser_subtract.set_defaults(func=subtract)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
