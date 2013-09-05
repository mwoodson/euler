#!/usr/bin/env ruby
#
#
load 'helper.rb'
require 'ruby-debug'
load 'result.rb'

def main
    results = []

    1.upto(300) do |num|
        result = Helper.triangle(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,0) 
    end

    1.upto(200) do |num|
        result = Helper.square(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,1)
    end

    1.upto(300) do |num|
        result = Helper.pentagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,2)
    end

    1.upto(200) do |num|
        result = Helper.hexagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,3)
    end

    1.upto(200) do |num|
        result = Helper.heptagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,4)
    end

    1.upto(300) do |num|
        result = Helper.octagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,5)
    end

    0.upto(results.size - 1).each do |ind|
        break if build_chain(ind, results)
    end
    
end

def build_chain(ind, results)
    start = 0
    index = [start]
    chain = Chain.new(results[ind], results[ind].id)


    while !chain.done?
        result = find_next(ind, start, results, chain)

        unless result.nil?
            if chain.chain.include?(results[result].id) || chain.path.collect { |z| z.value }.include?(results[result].value)
                #already there so we need to increment start 
                start = result + 1
            else
                chain.add_value(results[result]) 
                index << result
                ind = result
                start = 0
            end
        else
            #we found a solution but it stops the chain
            #pop the value and continue searching
            chain.rm_value 
            break if chain.chain.empty?
            lind = index.pop
            start = lind + 2
            ind = lind + 1
            break if ind >= results.size - 1
        end
    end

    if chain.done?
        pp chain.path 
        puts chain.sum
        return true
    end

    return false
end

def find_next(curr_ind, start, results, chain)
#puts curr_ind
    current = chain.path[-1]
    result = nil
    start.upto(results.size-1) do |ind|
        next if ind == curr_ind
        prospect = results[ind]
        # if it isn't cyclic, next
        next unless prospect.first == current.last
        # it is cyclic but is it in the same result set?
        next if prospect.id == current.id

        result = ind
        break
    end

    return result
end

if __FILE__ == $0
    main
end
