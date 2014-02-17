#!/usr/bin/env ruby
#
#
#

def solve(possible, all)
    not_it = []
    possible.each do |entry|
        all.each do |single|
            #is possible first?
            ind = single.index(entry)
            next if ind.nil?
            
            not_it << entry if possible.any? { |z|  ! single.index(z).nil? && single.index(z) < ind } 
        end
    end

    return possible - not_it
end


def next_possible(result, lines)
    possible = []
    #find all sequences starting with result
    lines.each do |line|
        line.strip!
        ind = line.index(result)
        next if ind.nil?

        possible << line[ind+1] if ind + 1 <= line.size - 1
    end

    return possible.uniq!
end

def main
    all_lines = []
    lines = File.open('keylog.txt').readlines()
    lines.uniq!
    lines.sort!

    answer = []

    possibilities=lines.collect { |line| line.strip!; line[0] }.uniq!

    arr_pos = 0
    while true
        puts "poss #{possibilities.inspect}"
        result = solve(possibilities, lines)
        raise "Inspect reult #{result.inspect}" if result.size != 1
        result = result.first
        puts "RESULT #{result} at arr[#{arr_pos}]"

        answer[arr_pos] = result
        arr_pos += 1
        possibilities = next_possible(result, lines)
        break if possibilities.nil? || possibilities.empty?
    end

    puts answer.inspect
end

if __FILE__ == $0
    main
end


__END__
main

 160
716

615
157



160
162
168
180
