#!/usr/bin/env python3
# coding: utf8

from FileProcesser.Reader import Reader
from FileProcesser.Writer import Writer

if __name__ == '__main__':
    print("input the name of the directory, it will read all the files.txt that's in it")
    folder_name = 'test'
    program_files_data = Reader.process_folder(folder_name)
    writer = Writer()
    writer.create_reports(program_files_data)