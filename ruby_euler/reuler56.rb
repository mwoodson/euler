#!/usr/bin/env ruby

require 'pp'


def main
    max = 0
    count = 0
    90.upto(99).each do |a|
        90.upto(99).each do |b|
            c = a**b
            count = c.to_s.split(//).collect{|n|n.to_i}.inject(:+)
            max = count if count > max
        end
    end
    puts max
end



if __FILE__ == $0
    main
end


__END__

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?


