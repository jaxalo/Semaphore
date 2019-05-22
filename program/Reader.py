#!/usr/bin/env python3
# coding: utf8

import os


class Reader:

    @staticmethod
    def process_folder(folder_name):
        print('opening : ', folder_name)
        program_files = []
        try:
            files_name = sorted(os.listdir('../' + folder_name))
            print('File to be processed :', ' ; '.join(files_name))
            for file_name in files_name:
                program_files.append(Reader.process_file(folder_name, file_name))
        except FileNotFoundError:
            print('Error : folder {} not found'.format(folder_name))
        return program_files

    @staticmethod
    def process_file(folder_name, file_name):
        try:
            file_path = '../' + folder_name + '/' + file_name
            with open(file_path) as fp:
                line = fp.readline()
                cnt = 1
                while line:
                    print("Line {}: {}".format(cnt, line.strip()))
                    line = fp.readline()
                    cnt += 1
            return True, None, file_name
        except Exception as e:
            print(e)
            return False, e, file_name
