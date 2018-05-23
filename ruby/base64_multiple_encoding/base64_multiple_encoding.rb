require 'base64'
require 'benchmark'

BLAH = 'hi'
ASCII_NUMS =  (0..255).to_a
ASCII_CHARS = ASCII_NUMS.map(&:chr)
MAX_ENCODING_COUNT = 20
FUNCTIONS = ['naieve_encoding_counts', 'improved_encoding_counts', 'prebuilt_encoding_counts']
PREBUILT_ENCODINGS = 1.upto(MAX_ENCODING_COUNT).inject({}) { |r, i| r[i] = Hash.new([]); r }

def get_ascii_encoding_path(max_encoding_count)
  ASCII_CHARS.inject({}) do |res, char|
    encoding_path = []
    max_encoding_count.times.inject(char)  do |r, encoding_count|
      encoded = Base64.encode64(r).strip
      encoding_path.push(encoded)
      encoded
    end

    res[char] = encoding_path
    res
  end  
end

def print_ascii_encoding_path(ascii_encoding_path)
  ascii_encoding_path.each do |key, value|
    n = 3
    final_encoding = value.map { |v| v.gsub('=', '') }.last
    first_n_chars = final_encoding[0..n] 
    puts "#{key.inspect}: first_#{n}_chars: #{first_n_chars }, length: #{final_encoding.length}"
  end
end

def naieve_encoding_counts
  1.upto(MAX_ENCODING_COUNT).inject({}) do |res, count|
    res[count] = get_ascii_encoding_path(count)
    res
  end
end

def improved_encoding_counts
  encodings = 1.upto(MAX_ENCODING_COUNT).inject({}) { |r, i| r[i] = Hash.new([]); r }
  ASCII_CHARS.each do |char|
    1.upto(MAX_ENCODING_COUNT).inject(char)  do |r, encoding_count|
      encoded = Base64.encode64(r).strip
      1.upto(encoding_count).each do |count|
        encodings[count][char].push(encoded)
      end
      encoded
    end
  end
  encodings
end

def prebuilt_encoding_counts 
  ASCII_CHARS.each do |char|
    1.upto(MAX_ENCODING_COUNT).inject(char)  do |r, encoding_count|
      encoded = Base64.encode64(r).strip
      1.upto(encoding_count).each do |count|
        PREBUILT_ENCODINGS[count][char].push(encoded)
      end
      encoded
    end
  end
  PREBUILT_ENCODINGS
end


Benchmark.bm(FUNCTIONS.map(&:length).max) do |x|
  FUNCTIONS.each { |label| x.report(label) { send(label) } }
end
