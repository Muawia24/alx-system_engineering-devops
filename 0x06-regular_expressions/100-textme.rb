#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flags:)\S+\w+\S+\w/).join(',')
