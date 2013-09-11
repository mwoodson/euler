#!/usr/bin/env ruby
=begin
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

=end

require 'pp' 
def main

    num_list = File.open('triangle.txt').read.split("\n").collect! do |line|
        line.split.map(&:to_i)
    end


    last_sums = num_list.last
    (num_list.size-2).downto(0).each do |x|
        #for simplicity
        cur_row = num_list[x]
        last_row = num_list[x+1]

        curr_sums = []

        cur_row.each_with_index do |num,r_ind|
           curr_sums << last_sums[(r_ind..r_ind+1)].max + num
        end

        last_sums = curr_sums
    end
    pp last_sums
end

if __FILE__ == $0
    main
end
