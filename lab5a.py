#!/usr/bin/env python3

def read_file_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()  # Reads the entire content as a string

def read_file_list(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]  # Reads the file as a list, removing newline characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

