#!/usr/bin/env ruby
f, t, fl = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).flatten
puts f+","+t+","+fl
