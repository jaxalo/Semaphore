#!/usr/bin/env python3
# coding: utf8

import sys

from FileProcesser.Reader import Reader
from FileProcesser.Writer import Writer

if __name__ == '__main__':
    name = sys.argv[1]
    if name.endswith('.txt'):
        file_name = name
        program_files_data = Reader.process_file_only_one(file_name)
    else:
        folder_name = name
        program_files_data = Reader.process_folder(folder_name)

    writer = Writer()
    writer.create_reports(program_files_data)
