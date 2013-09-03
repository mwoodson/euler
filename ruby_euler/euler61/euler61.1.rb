#!/usr/bin/env ruby
#
#
load 'helper.rb'
require 'ruby-debug'

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
    trif    = Hash.new(Array.new)
    tril    = Hash.new(Array.new)
    sqf     = Hash.new(Array.new)
    sql     = Hash.new(Array.new)
    pentf   = Hash.new(Array.new)
    pentl   = Hash.new(Array.new)
    hexf    = Hash.new(Array.new)
    hexl    = Hash.new(Array.new)
    heptf   = Hash.new(Array.new)
    heptl   = Hash.new(Array.new)
    octf    = Hash.new(Array.new)
    octl    = Hash.new(Array.new)

    trif['id']  ='trif'
    tril['id']  ='tril'
    sqf['id']   ='sqf'
    sql['id']   ='sql'
    pentf['id'] ='pentf'
    pentl['id'] ='pentl'
    hexf['id']  ='hexf'
    hexl['id']  ='hexl'
    heptf['id'] ='heptf'
    heptl['id'] ='heptl'
    octf['id']  ='octf'
    octl['id']  ='octl'

    tri  = []
    sq   = []
    pent = []
    hex  = []
    hept = []
    oct  = []
=begin
        8128 tri_last_two = 28
        2882 prev_last_two == my_first_two 
        8281 prev_last_two == my_first_two
=end
    1.upto(300) do |num|
        result = Helper.triangle(num)
        next if result < 1000
        break if result > 9999
        last_two  = result.to_s[-2..-1]
        first_two = result.to_s[0..1]
        tri << result
        tril[last_two] += [result]
        trif[first_two] += [result]
    end

#puts "TRI:"
#pp tri
    1.upto(200) do |num|
        result = Helper.square(num)
        next if result < 1000
        break if result > 9999
        last_two  = result.to_s[-2..-1]
        first_two = result.to_s[0..1]
        sq << result
        sql[last_two] += [result]
        sqf[first_two] += [result]
    end

#puts "SQ"
#pp sq

    1.upto(300) do |num|
        result = Helper.pentagonal(num)
        next if result < 1000
        break if result > 9999
        last_two  = result.to_s[-2..-1]
        first_two = result.to_s[0..1]
        pent << result
        pentl[last_two] += [result]
        pentf[first_two] += [result]
    end

#puts "PENT"
#pp pent
#pp tmp & a
#exit

    1.upto(200) do |num|
        result = Helper.hexagonal(num)
        next if result < 1000
        break if result > 9999
        last_two = result.to_s[-2..-1]
        first_two = result.to_s[0..1]
        hex << result
        hexl[last_two] += [result]
        hexf[first_two] += [result]
    end

#puts "HEX"
#pp hex

    1.upto(200) do |num|
        result = Helper.heptagonal(num)
        next if result < 1000
        break if result > 9999
        last_two = result.to_s[-2..-1]
        first_two = result.to_s[0..1]
        hept << result
        heptl[last_two] += [result]
        heptf[first_two] += [result]
    end

#puts "HEPT"
#pp hept

    1.upto(200) do |num|
        result = Helper.octagonal(num)
        next if result < 1000
        break if result > 9999

        last_two = result.to_s[-2..-1]
        first_two = result.to_s[0..1]

        oct << result
        octf[first_two] += [result]
        octl[last_two] += [result]
    end

#puts "OCT"
#pp oct
#Is it in tri first?
#pp tril.count
$llast = [tril, sql, pentl, hexl, heptl]
$lfirst = [trif, sqf, pentf, hexf, heptf]

list = nil
last = true
    octl.each do |key, values|
        next if key == 'id' || key == '00'

        list = get_list(last)

        last = !last

        results = search(key, list)

        results.each do |result|
            pos, value  = 
            
        end

        exit
        

        
    end

        
#puts "KEY=>#{last}"
#list.each do |dict|
#puts "#{dict['id']} => #{dict[last]}" if dict[last].length > 0
#end
#
#last = !last
#break
#end
#
end
def get_list(last)
    unless last
        list = $llast
    else
        list = $lfirst
    end
    return list
end


def search(value, list)
    rvals = []
    0.upto(list.length - 1).each do |num|
        if list[num][value].length > 0
            puts "#{list[num]['id']} => #{list[num][value]}" 
            rvals <<  [num, list[num][value]]
        end
    end

    return rvals
end

if __FILE__ == $0
    main
end
