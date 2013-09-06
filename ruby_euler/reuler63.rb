#!/usr/bin/env ruby

require 'pp'
#relative_require 'lib/helper'
require_relative 'lib/helper'

=begin
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
=end

def main
    a = '1' + '0' * 9
    puts a.to_i
    a = '20000'
    results = []
    1.upto(21).each do |pow|
        1.upto(99).each do |x|
            result = x ** pow
            length = result.to_s.size
#puts "length=>#{length} result=>#{result} #{pow}" if x == 7
            if length == pow
                puts "x(#{x}) pow(#{pow}) => length(#{length}) result(#{result})"
                results << result
            elsif length > pow
                break
            end
        end
    end
    
    puts results.length
end

if __FILE__ == $0
    main
end
