#!/usr/bin/env ruby

require 'pp'
require 'mathn'

def better_sieve_upto(n)
  s = (0..n).to_a
  s[0] = s[1] = nil
  s.each do |p|
    next unless p
    break if p * p > n
    (p*p).step(n, p) { |m| s[m] = nil }
  end
  s.compact
end


def prime(n)
    return false if n % 2 == 0
    (3..((n**0.5).to_i + 1)).step(2).each do |s|
        return false if n % s == 0
    end
    return true
end

def main
    
    #primes = Prime.instance
    moves = 2
    diag = 1
    c = 1
    pc = 0
    z = 100
    corners = []
    #see if our percentage is met
    while z > 0.10 && c > 0
        0.upto(3).each do |ind| 
            c += moves
            pc += 1 if prime(c)
            diag += 1
        end
        moves += 2
        z = (pc / diag).to_f
    end
    puts "Iteration: #{c **0.5}: c=#{c} z=#{z}"
end

if __FILE__ == $0
    main
end


__END__

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?



=begin
#go right
1 1 1
#go up
1 d 3 5
#go left
2 d 4 6
#go down
2 d 4 6
#go right
2 d 4 6
=end
