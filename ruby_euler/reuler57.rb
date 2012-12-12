#!/usr/bin/env ruby

require 'pp'


def main

    count = 0
    a = 3
    b = 2
    old_a = 1
    old_b = 1
    tmp_a = 1
    tmp_b = 1
    1.upto(1000).each do |num|
#puts "#{a}/#{b} => #{a/b.to_f}"
        old_a = a
        old_b = b
        a = a * 2 + tmp_a
        b = b * 2 + tmp_b
        tmp_a = old_a
        tmp_b = old_b
        count += 1 if a.to_s.length > b.to_s.length 
    end

    puts count
end




if __FILE__ == $0
    main
end


__END__


It is possible to show that the square root of two can be expressed as an infinite continued fraction.

 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

 By expanding this for the first four iterations, we get:

 1 + 1/2 = 3/2 = 1.5
 1 + 1/(2 + 1/2) = 7/5 = 1.4
 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

 The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

 In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?



#>> eval("1+1/(2+1/" * 3 + "2" + ").to_f" * 3)
3/2 => *2+1

7/5 => *2+3 / *2 + 2

17/12 * 2 + 7 / * 2 + 5

41/29
