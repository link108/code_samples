__author__ = 'cmotevasselani'
# Testing script


from n_gram import NGram
import time

n_gram = NGram()
n_gram.data = NGram.create_string_from_files("resources/words")
n_gram.n = 2

start = time.time()
n_gram.n_gram_map = NGram.create_n_gram_map(n_gram.n)
end = time.time()
NGram.calculate_n_grams(n_gram.n, n_gram.n_gram_map, n_gram.data)

time_diff = end - start
print 'Time taken: ' + str(time_diff) + ' seconds'


non_zero_n_grams = NGram.get_non_zero_n_grams(n_gram.n_gram_map, to_print=True)
zero_n_gram_list = NGram.get_zero_n_grams(n_gram.n_gram_map, to_print=True)

print 'total num n_grams: ' + str(len(n_gram.n_gram_map.keys()))
print 'num non-zero n_grams: ' + str(len(non_zero_n_grams.keys()))






