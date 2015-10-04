__author__ = 'cmotevasselani'

from urlparse import urlparse, parse_qs

filename = "data/test"
output_file = "data/tmp"

# file char by char
with open(filename) as f:
    for line in f:
        print 'line: ' + line
        for char in line:
            print 'char: ' + char

# file word by word
with open(filename) as f:
    for line in f:
        print 'line: ' + line
        for word in line.split(' '):
            print 'word: ' + word


# url stuff
url = urlparse("http://byah.org:8080/sample/test?with=query&params=byah")
params = parse_qs(url.query)
print 'url: ' + url


# list

num_list = [1, 2, 3, 4, 5]
string_list = ["one", "two", "three", "four", "five"]
char_list = ['a', 'b', 'c', 'd', 'e']

for item in num_list:
    print item
print 'size of list: ' + str(len(num_list))
with open(output_file, 'a') as f:
    for word in string_list:
        f.write(str(word) + '\n')


for i in range(5):
    print 'i: ' + str(i)
print 'size of range: ' + str(len(range(5)))






# dict

varied_hash = {'foo': 'bar', 'int': 5, 'string': 'byah', 'list': [1, 2, 3, 4, 5], 'tuple': ('a', 1)}

for key in varied_hash.keys():
    print 'key: ' + str(key)
    print 'value: ' + str(varied_hash[key])



# set

num_set = set([1,2,3,4,5])
num_set.add(1)
print 'num_set: ' + str(num_set)


# tuple
string_tuple = ('first', 'second')
int_tuple = (1, 2, 3, 4, 5)
for item in int_tuple:
    print item
print 'size of tuple: ' + str(len(int_tuple))



# Map and functions

def add2(x):
    return x+2

def mult2(x):
    return x*2

def pow2(x):
    return x**2


x = map(add2, num_list)
y = [add2(item) for item in num_list]
print 'x: ' + str(x)
print 'y: ' + str(y)



x = map(mult2, num_list)
y = [mult2(item) for item in num_list]
print 'x: ' + str(x)
print 'y: ' + str(y)



x = map(pow2, num_list)
y = [pow2(item) for item in num_list]
print 'x: ' + str(x)
print 'y: ' + str(y)


