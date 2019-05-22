#!/usr/bin/env python3
# coding: utf8

from program.Reader import Reader
from program.Writer import Writer

if __name__ == '__main__':
    print("input the name of the directory, it will read all the files.txt that's in it")
    folder_name = 'test'
    program_files = Reader.process_folder(folder_name)
    writer = Writer()
    for success, program_file, file_name in program_files:
        writer.create_report(success, program_file, file_name)
