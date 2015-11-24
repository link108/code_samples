
import os
from os import listdir
from os.path import isfile, join
from string import ascii_lowercase


class NGram:

    def __init__(self):
        self.n_gram_map = None
        self.data = None
        self.n = None

    @staticmethod
    def create_n_gram_map(n):
        n_gram_map = {}
        n_grams = NGram.create_n_gram_strings(n)
        for key in n_grams:
            n_gram_map[key] = 0
        return n_gram_map

    @staticmethod
    def create_n_gram_strings(n):
        n_grams = []
        for i in range(n):
            n_grams = NGram.add_to_n_gram_array(n_grams)
        return n_grams

    @staticmethod
    def add_to_n_gram_array(n_grams, to_add=ascii_lowercase + '- '):
        n_grams_to_add = []
        if len(n_grams) == 0:
            n_grams_to_add.extend([key for key in to_add])
        else:
            for n_gram in n_grams:
                for char in to_add:
                    new_n_gram = n_gram + char
                    n_grams_to_add.append(new_n_gram)
        return n_grams_to_add

    @staticmethod
    def calculate_n_grams(n, n_gram_map, data):
        data_array = [letter for letter in data]
        for start_index in range(len(data_array) - n):
            end_index = start_index + n
            n_gram = ''.join(data_array[start_index:end_index]).lower()
            n_gram_map[n_gram] += 1
        return n_gram_map

    @staticmethod
    def convert_file_to_string(file_location):
        with open(file_location, "r") as my_file:
            data = my_file.read().replace('\n', ' ')
        return data

    @staticmethod
    def create_string_from_files(file_location):
        expected_data = ''
        if os.path.isfile(file_location):
            files = [file_location]
        elif os.path.isdir(file_location):
            files = [file_location + '/' + f for f in listdir(file_location) if isfile(join(file_location, f))]
        else:
            raise Exception
        for file_name in files:
            expected_data += NGram.convert_file_to_string(file_name)
        return expected_data

    @staticmethod
    def get_non_zero_n_grams(n_gram_map, to_print=False):
        non_zero_n_gram_map = {}
        for key in n_gram_map.keys():
            if n_gram_map[key] != 0:
                if to_print:
                    print 'n-gram: ' + str(key) + ' occurred ' + str(n_gram_map[key]) + ' times'
                non_zero_n_gram_map[key] = n_gram_map[key]
        return non_zero_n_gram_map

    @staticmethod
    def get_zero_n_grams(n_gram_map, to_print=False):
        zero_n_gram_list = []
        for key in n_gram_map.keys():
            if n_gram_map[key] == 0:
                if to_print:
                    print 'n-gram: ' + str(key) + ' did not occur'
                zero_n_gram_list.append(key)
        return zero_n_gram_list


    @staticmethod
    def calculate_n_grams_with_empty_map(n, n_gram_map, data):
        data_array = [letter for letter in data]
        for start_index in range(len(data_array) - n):
            end_index = start_index + n
            n_gram = ''.join(data_array[start_index:end_index]).lower()
            if n_gram in n_gram_map:
                n_gram_map[n_gram] += 1
            else:
                n_gram_map[n_gram] = 1
        return n_gram_map

    @staticmethod
    def print_all_n_grams(n_gram_map):
        for key in n_gram_map.keys():
            print 'n-gram: ' + str(key) + ' occurred ' + str(n_gram_map[key]) + ' times'

