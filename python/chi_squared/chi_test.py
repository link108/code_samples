
import math
import os
from os import listdir
from os.path import isfile, join, isdir


class ChiTest:

    def __init__(self):
        self.expected = [0] * 256
        self.observed = [0] * 256

    @staticmethod
    def create_histogram_array(hist_array, observed_data):
        for char in observed_data:
            hist_array[ord(char)] += 1

    @staticmethod
    def get_frequencies(expected):
        total, frequencies = ChiTest.get_size_and_freq_array(expected)
        for index in range(len(expected)):
            frequencies[index] = expected[index] / total
        return frequencies

    # observed is an array of floats
    @staticmethod
    def create_estimated_frequency(observed, frequencies):
        total, estimated_frequency = ChiTest.get_size_and_freq_array(observed)
        for index in range(len(observed)):
            estimated_frequency[index] = frequencies[index] * total
        return estimated_frequency

    @staticmethod
    def get_size_and_freq_array(data):
        total = 0
        frequencies = [0] * len(data)
        for index in range(len(data)):
            total += data[index]
        return total, frequencies

    @staticmethod
    def pearson_chi_test(observed, expected):
        if len(observed) != len(expected):
            return None
        if sum(observed) != sum(expected):
            print 'sums are not equal'
            print 'sum(observed): ' + str(sum(observed))
            print 'sum(expected): ' + str(sum(expected))
        chi_squared = [0] * len(expected)
        for index in range(len(expected)):
            if expected[index] != 0 and observed[index] != 0:
                deviation = observed[index] - expected[index]
                deviation_squared = math.pow(deviation, 2)
                chi_squared[index] = deviation_squared / expected[index]
        chi_squared_total = sum(chi_squared)
        return chi_squared_total

    @staticmethod
    def convert_file_to_string(file_location):
        with open(file_location, "r") as myfile:
            data=myfile.read().replace('\n', '')
        return data

    @staticmethod
    def create_expected_data(file_location):
        expected_data = ''
        if os.path.isfile(file_location):
            files = [file_location]
        elif os.path.isdir(file_location):
            files = [ file_location + '/' + f for f in listdir(file_location) if isfile(join(file_location,f)) ]
        for file in files:
            expected_data += ChiTest.convert_file_to_string(file)
        return expected_data


chi_test = ChiTest()
expected_data = ChiTest.create_expected_data("resources/expected")
observed_data = ChiTest.create_expected_data("resources/observed")
ChiTest.create_histogram_array(chi_test.expected, expected_data)
ChiTest.create_histogram_array(chi_test.observed, observed_data)
# normalized_observed, normalized_expected = ChiTest.normalize_data(chi_test.observed, chi_test.expected)
normalized_observed, normalized_expected = chi_test.observed, chi_test.expected
frequencies = ChiTest.get_frequencies(normalized_expected)
estimated_frequencies = ChiTest.create_estimated_frequency(normalized_observed, frequencies)
pearson_chi_squared = ChiTest.pearson_chi_test(normalized_observed, normalized_expected)
print 'pearson_chi_squared: ' + str(pearson_chi_squared)

# create observed
# get frequencies of observed => array of floats
# generate estimated frequencies => array of ints, sum of ints == num chars in string
# test

