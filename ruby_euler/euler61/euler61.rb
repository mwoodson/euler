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
a = [1281, 8128, 2882, 8256, 5625, 2512]
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

    0.upto(results.size - 1).each do |ind|
        pp results[ind]
        build_chain(ind, results)
        break
    end
    
end

def build_chain(ind, results)
        current = results[ind]
        chain = Chain.new(current, current.id)

        debugger
        begin
            search_id = chain.next_attempt
            puts search_id
            break if search_id.nil?
            possibilities = results.select do |result|
                result if result != current && current.last == result.first && search_id == result.id
            end

            pp possibilities if possibilities.size > 0

            chain.add_attempt(search_id)

            
        end while true

end

if __FILE__ == $0
    main
end
