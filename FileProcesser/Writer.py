#!/usr/bin/env python3
# coding: utf8

from pathlib import Path
import os


class Writer:
    folder_name = '../report'

    def __init__(self):
        pth = Path(self.folder_name)
        for sub in pth.iterdir():
            if sub.is_dir():
                self.delete_folder(sub)
            else:
                sub.unlink()

    def create_reports(self, program_files):
        for success, program_file, file_name in program_files:
            self.create_report(success, program_file, file_name)

    def create_report(self, success, program_file, file_name):
        path = os.getcwd() + '/' + self.folder_name
        if not os.path.exists(path):
            os.makedirs(path)

        file_create = 'Report_' + file_name
        with open(os.path.join(path, file_create), 'w+') as temp_file:
            temp_file.write('Success\n' if success else 'Fail\n')
            temp_file.write('\n')
            if success:
                temp_file.write(program_file)
            else:
                temp_file.write(str(program_file))

    def delete_folder(self, pth):
        for sub in pth.iterdir():
            if sub.is_dir():
                self.delete_folder(sub)
            else:
                sub.unlink()
