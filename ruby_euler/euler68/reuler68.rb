#!/usr/bin/env ruby
#
#
# If we want to maximize our value for our string then we will
# need to start with the highest numbers on the outside of
# the 5-gon.  This will at least guarantee we have larger
# numbers.  That gives us 10-6 on the outer nodes and 
# leaves 1-5 on the inner nodes.
#
#     10-5-4 = 19
#     9-3-2 = 15
#
# Figuring out the shape is a matter of trial and error until
# all / any of the 5 chains equal the same value.
#
# Magically after enough white boarding and trial and error, 
# we come up with the #14.
#
# That means:
# 10 3 1 = 14
#  9 1 4 = 14
#  8 4 2 = 14
#  7 2 5 = 14
#  6 5 3 = 14
#
# This easily produces the solution we need because we would
# start with the lowest number on the outside of the 5-gon
# which is 6.  Then try to maximize then number so we 
# then proceed to 10,3,1 and to the next highest 9,1,4 and
# so on.  
#
# 6,5,3,10,3,1,9,1,4,8,4,2,7,2,5

#6531031914842725
#
# In order to brute force this solution you will need to 
# take all numbers starting with 6-10 (maximize remember) 
# and create permutations with numbers 1-5 creating a set 
# where all values sum to the same value for all sets.
#
# Let's take a stab at this
#
require 'pp'

def main
    results = {}
    inner_ring = (1..5).to_a
    (6..10).each do |num|
        results[num] = {}
        #get permutations 2 at a time
        perms = inner_ring.permutation(2)
        perms.each do |p|
            result = num + p.inject(:+)
            results[num][result] ||= []
            results[num][result] << p.sort!
            results[num][result].uniq!
        end
    end

    pp results

    possibilities = results[6].keys

    results.each do |outer,outer_solutions|
        results.each do |out, solutions|
            next if outer == out
            possibilities &= solutions.keys
        end
    end

    totals = {}

    possibilities.each do |num|
        totals[num] = []
        results.each do |outer, solutions|

            z = results[outer][num].collect do |sol| 
                sol.insert(0,outer)
            end
            puts "z=>#{z.inspect}"
#z.insert(0, outer)
            totals[num] << z
#results[outer][num].map! { |sol| sol.insert(0,outer) }
        end
    end

    pp totals

    #Since we have to start with the lowest number in the
    #outer ring we must select the solutions for 6 first.
    #This gives us 3 different solutions
#all_perms = []
#totals.each do |key, arr|
        #start with the 6 array
#path = []
#0.upto(arr.size - 1).each do |num|
#0.upto(arr[num].size-1).each do |ind|
#path << arr[num][ind]
#end
#pp path
#end
#first.each do |f|
##start with each 6
#0.upto(
#
#end
    

#end
    pp select(totals[14])

=begin
    totals.keys.each do |sol|
        arr = totals[sol]
        first = arr.first
        a = arr.delete(first)
        arr = arr.sort { |x,y| x[0] <=> y[0] }.reverse
        a += arr.flatten
        puts a.join('')
    end

    totals.each do |sum, arr|
        #start with 6's possible solutions
        for arr[0].each do |sol_6|
            num = []
            num << sol_6.flatten
            1.upto(arr.size-1).each do |ind|
                arr[ind]
            end

            
        end
    end
=end
end

def select(array, path=[])
    return array if path.size == 5
    return array if array[0].is_a?(Fixnum)

    0.upto(array.size-1).each do |num|
        arr = array[num]
        arr.each do |a|
            path << a
            select(array[(num..-1)], path)
        end
    end
end

if __FILE__ == $0
    main
end
