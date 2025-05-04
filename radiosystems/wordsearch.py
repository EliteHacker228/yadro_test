import argparse
import sys

parser = argparse.ArgumentParser(description='Search a word in a file')

parser.add_argument('-f', '--file', required=True, help='Path to file to parse')
parser.add_argument('-w', '--word', required=True, help='Word to search in file')

args = parser.parse_args()

file_path = args.file
search_word = args.word

try:
    with open(file_path, 'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            if search_word in line:
                print(line, end='')
        print('')
        sys.exit(0)
except FileNotFoundError:
    print(f'ERROR: file {file_path} not found')
    sys.exit(1)
except Exception as e:
    print(f'ERROR: unhandled exception {type(e).__name__} was acquired')
    sys.exit(1)
