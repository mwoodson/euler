#!/usr/bin/env ruby
#
#
load 'helper.rb'
require 'ruby-debug'

def main
=begin
    tri_results = []
    45.upto(150) do |num|
        tri_results << Helper.triangle(num)
        break if num > 9999
    end
=end
a = [1281, 8128, 2882, 8256, 5625, 2512]
    numbers = []
    tri  = Array.new
    sq   = Array.new
    pent = Array.new
    hex  = Array.new
    hept = Array.new
    oct  = Array.new

    chain = []

    1.upto(300) do |num|
        result = Helper.triangle(num)
        next if result < 1000
        break if result > 9999
        tri << result
    end

#puts "TRI:"
#pp tri
#
    1.upto(200) do |num|
        result = Helper.square(num)
        next if result < 1000
        break if result > 9999
        sq << result
    end

#puts "SQ"
#pp sq

    1.upto(300) do |num|
        result = Helper.pentagonal(num)
        next if result < 1000
        break if result > 9999
        pent << result
    end

#puts "PENT"
#pp pent
#pp tmp & a
#exit

    1.upto(200) do |num|
        result = Helper.hexagonal(num)
        next if result < 1000
        break if result > 9999
        hex << result
    end

#puts "HEX"
#pp hex

    1.upto(200) do |num|
        result = Helper.heptagonal(num)
        next if result < 1000
        break if result > 9999
        hept << result
    end

#puts "HEPT"
#pp hept

    1.upto(300) do |num|
        result = Helper.octagonal(num)
        next if result < 1000
        break if result > 9999
        oct << result
    end


pp oct.count
    
end

def first(input)
    return input.to_s[0..1]
end

def last(input)
    return input.to_s[-2..-1]
end

if __FILE__ == $0
    main
end
