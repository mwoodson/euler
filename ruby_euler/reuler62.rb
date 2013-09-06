#!/usr/bin/env ruby

require 'pp'
#relative_require 'lib/helper'
require_relative 'lib/helper'

=begin
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
=end

def main
    results = {}
    strings = Hash.new(Array.new)
    0.upto(10000).each do |ind|
        result = Helper.to_power_3(ind)
        results[ind] = result
        key = result.to_s.split(//).sort.join
        strings[key] += [ind]
        if strings[key].size == 5
            puts strings[key][0] 
            puts results[strings[key][0]]
            break
        end
        
    end

#puts results[345]
#puts results[384]
#puts results[405]

#strings.each do |key,value|
#pp results[value[0]] if value.length == 5
#end
    
end

if __FILE__ == $0
    main
end
