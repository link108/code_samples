require 'open-uri'
require 'rubygems'
require 'work_queue'

#num_threads = ARGV[0].to_i

%w(1 2 5 10 15 20 25 50).each do |num_threads|
  wq = WorkQueue.new num_threads.to_i

  start_time = Time.now
  (1..1000).each do |number|
    wq.enqueue_b do
      open("temp/rfc#{number}.txt", "wb") do |file|
        file.write(' ')
      end
    end
  end
  wq.join
  end_time = Time.now()
  empty_file_create_time = end_time - start_time

  puts "Number threads: #{num_threads}"
  puts "Empty file create time taken: #{empty_file_create_time}"

  files_to_remove = Dir.glob('temp/*')

  start_time = Time.now
  files_to_remove.each do |file|
    wq.enqueue_b do
      File.delete(file)
    end
  end
  wq.join
  end_time = Time.now
  empty_file_delete_time = end_time - start_time

  puts "Empty file delete time taken: #{empty_file_delete_time}"


end

