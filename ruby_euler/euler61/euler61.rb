#!/usr/bin/env ruby
#
#
load 'helper.rb'
require 'ruby-debug'
load 'result.rb'

def main
=begin
    tri_results = []
    45.upto(150) do |num|
        tri_results << Helper.triangle(num)
        break if num > 9999
    end
=end
#a = [1281, 8128, 2882, 8256, 5625, 2512]
    numbers = []
    tri  = Array.new
    sq   = Array.new
    pent = Array.new
    hex  = Array.new
    hept = Array.new
    oct  = Array.new

    results = []

    1.upto(300) do |num|
        result = Helper.triangle(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,0)
    end

#puts "TRI:"
#pp tri
#
    1.upto(200) do |num|
        result = Helper.square(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,1)
#sq << result
    end

#puts "SQ"
#pp sq

    1.upto(300) do |num|
        result = Helper.pentagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,2)
#pent << result
    end

#puts "PENT"
#pp pent
#pp tmp & a
#exit

    1.upto(200) do |num|
        result = Helper.hexagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,3)
#hex << result
    end

#puts "HEX"
#pp hex

    1.upto(200) do |num|
        result = Helper.heptagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,4)
#hept << result
    end

#puts "HEPT"
#pp hept

    1.upto(300) do |num|
        result = Helper.octagonal(num)
        next if result < 1000
        break if result > 9999
        results << Result.new(result,5)
#oct << result
    end
    $debug = false

    debugger 
    0.upto(results.size - 1).each do |ind|
        print "\nSTART: #{results[ind].value}: "
        if results[ind].value == 1281
            $debug = true
        end

        build_chain(ind, results)
    end
    
end

def build_chain(ind, results)
    start = 0
    current = results[ind]
    last_ind = ind
    chain = Chain.new(current, current.id)


    while !chain.done?
#puts "IND=>#{ind} Start=>#{start}"
        result = find_next(ind, start, results)

        unless result.nil?
            if chain.chain.include?(results[result].id)
                #already there so we need to increment ind 
                ind += 1
                break if ind >= results.size
            else
                print " #{results[result].value}, "
                chain.add_value(results[result]) 
                last_ind = ind
#pp chain.chain
                ind = result
                start = 0
            end
        else
            break if ind == results.size - 1
            #we found a solution but it stops the chain
#puts "removing last chain.chain[-1] => #{chain.chain[-1]}"
            chain.rm_value 
            break if chain.chain.empty?
            start = last_ind + 1
            ind = last_ind
            current = chain.chain[-1]
        end
    end

    pp chain.path if chain.done?
    return chain.done?
end

def find_next(curr_ind, start, results)
#puts curr_ind
    current = results[curr_ind]
    result = nil
    start.upto(results.size-1) do |ind|
        next if ind == curr_ind
        prospect = results[ind]
        # if it doesn't match letters, next
        next unless prospect.first == current.last
        # if the id is the same or already is in the chain, go next
        next if prospect.id == current.id

        debugger if $debug
        result = ind
        break
    end

#puts result
    return result
end

if __FILE__ == $0
    main
end
