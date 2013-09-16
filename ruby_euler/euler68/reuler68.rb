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
#results[num][result] << p.sort!
            results[num][result] << p
            
            results[num][result].uniq!
        end
    end

    possibilities = results[6].keys

    #search each solution and only include results found in each array
    #13,14,15 are found in all therefore these are possibilities for the
    #sum of the leg
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
            totals[num] << z
        end
    end


    #format the arrays the way we want them, basically flatten them if they are length 1
    totals.each do |key,arr|
        arr.collect! do |values|
            values.flatten! if values.size == 1
            values
        end
        totals[key] = arr
    end


#    #We now have the possibilities, we just need to rearrange them into the correct order
#    #Inner circle!
#    totals.each do |key,arr| 
#        0.upto(arr.size-1).each do |num|
#            poss = []
#            if arr[num][0].is_a?(Array) 
#                arr[num].each do |z|
#                    poss << z
#                    poss << [z[0],z[2], z[1]]
#                end
#            else
#                poss << arr[num] 
#                poss << [arr[num][0],arr[num][2], arr[num][1]]
#            end
#            totals[key][num] = poss
#        end
#    end

    #based on the possibilities for each sum (13,14,15), build all paths
    results = []
    totals.each do |key,value| 
        results += select(value)
    end

    #filter the results for the correct inner circle
    results.collect! do |result|
        result if check_positions(result)
    end

    results.compact!

    #now comb the results and build the strings we want
    #this builds a string from the possible values
    #and prints the maximum value of it
    results.collect! do |result|
        first = result.first
        result.delete(first)
        result.sort_by! {|a| a[0]}.reverse!
        puts "sresults=>#{result.inspect}"
        (first.join + result.join ).to_i
    end

    pp results.max
end

#This is the inner circle verifier.  You cannot have 
#a number repeated in the same position in an array
def check_positions(array)
    array.each do |a|
        array.each do |b|
            next if a == b
            return false if a[1] == b[1] || a[2] == b[2]
        end
    end

    return true
end

#Recursively build a valid path of length 5
def select(array, path=[], solutions=[])
    if path.size == 5 #|| array.size == 0
        solutions << path
        return solutions 
    end

    0.upto(array.size-1).each do |num|
        arr = array[num]
        if arr[0].is_a?(Array)
            arr.each do |a|
                select(array[(num+1..-1)], path + [a],solutions)
            end
        else
            select(array[(num+1..-1)], path + [arr], solutions)
        end
    end

    return solutions
end

if __FILE__ == $0
    main
end
