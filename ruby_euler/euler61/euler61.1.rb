#!/usr/bin/env ruby
#
#
load 'helper.rb'
require 'ruby-debug'
load 'result.rb'

class MyResult
    attr_accessor :results

    def initialize
        @results = []
    end

    def calculate!(ind, code)
        1.upto(300) do |n|
            result = code.call(n)
            next if result < 1000
            break if result > 9999
            @results << Result.new(result,ind)
        end
    end
end

def main
    myresult = MyResult.new
    [:triangle, :square, :pentagonal, :hexagonal, :heptagonal, :octagonal].each_with_index do |sym, ind|
        myresult.calculate!(ind, Helper.method(sym) )
    end
    0.upto(myresult.results.size - 1).each do |ind|
        break if build_chain(ind, myresult.results)
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
