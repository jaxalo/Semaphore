#!/usr/bin/env python3
# coding: utf8

import os
from program.PartialProcess import PartialProcess
from FileProcesser.Analyser import Analyser
from program.Scheduler import Scheduler


class Reader:
    SEPARATOR = '\n------------------------------\n'

    @staticmethod
    def process_folder(folder_name):
        print('opening : ', folder_name)
        program_files = []
        try:
            files_name = sorted(os.listdir('../' + folder_name))
            print('File to be processed :', ' ; '.join(files_name))
            for file_name in files_name:
                if file_name.endswith('.txt'):
                    program_files.append(Reader.process_file1(folder_name, file_name))
        except FileNotFoundError:
            print('Error : folder {} not found'.format(folder_name))
        return program_files

    @staticmethod
    def process_file(folder_name, file_name):
        try:
            file_path = '../' + folder_name + '/' + file_name
            process = PartialProcess()
            analyser = Analyser()
            with open(file_path) as fp:
                print(Reader.SEPARATOR, file_name)
                process.build(fp)
                analyser.analyse_syntax(process)
                analyser.analyse_semantic(process)
                if analyser.is_correct():
                    res = process.serialize()
                else:
                    res = analyser.get_errors()
                print('done_processing ', file_name, Reader.SEPARATOR)
                return analyser.is_correct(), res, file_name
        except Exception as e:
            print('done_processing ', file_name, Reader.SEPARATOR)
            return False, e, file_name

    @staticmethod
    def process_file1(folder_name, file_name):
        try:
            file_path = '../' + folder_name + '/' + file_name
            process = PartialProcess()
            analyser = Analyser()
            with open(file_path) as fp:
                print(Reader.SEPARATOR, file_name)
                process.build(fp)
                analyser.analyse_syntax(process)
                analyser.analyse_semantic(process)
                # build process
                print('done_processing ', file_name, Reader.SEPARATOR)
                if analyser.is_correct():
                    scheduler = Scheduler(process)
                    scheduler.run_simulations()
                    print('all simulation done')
                    res = scheduler.get_str_result()
                else:
                    res = analyser.get_errors()
                return analyser.is_correct(), res, file_name

        except Exception as e:
            print('done_processing ', file_name, Reader.SEPARATOR)
            return False, e, file_name
