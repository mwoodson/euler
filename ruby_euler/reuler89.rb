#!/usr/bin/env ruby
#
#
#
class RomanNumeral
    @@roman= {
        "M"  => 1000,
        "CM" => 900,
        "D"  => 500,
        "CD" => 400,
        "C"  => 100,
        "XC" => 90,
        "L"  => 50,
        "XL" => 40,
        "X"  => 10,
        "IX" => 9,
        "V"  => 5,
        "IV" => 4,
        "I"  => 1,
    }

    attr_accessor :decimal, :roman_numeral, :left_to_right

    def initialize(input)
        @original = input
        @decimal = to_decimal(@original)
        @roman_numeral = to_roman(@decimal)
    end
    
    def saved()
        return @original.size - @roman_numeral.size
    end
    
    def order
        return @@roman[@original[0]] >= @@roman[@original[-1]]
    end

    def to_decimal(original)
        result = 0
        skip = false

        (original.size-1).downto(0).each do |pos|
            if skip
                skip = false
                next 
            end

            if pos > 0
                if @@roman[original[pos]] > @@roman[original[pos-1]]
                    result -= @@roman[original[pos-1]] - @@roman[original[pos]]
                    skip = true
                    next
                    
                end
            end
            result += @@roman[original[pos]]
        end

        return result
    end

    #rules
    #1. Only I, X, and C can be used as the leading numeral in part of a subtractive pair
    #2. I can only be placed before V and X
    #3. X can only be placed before L and C
    #4. C can only be placed before D and M

    def to_roman(num)
        ans = []
        while(num > 0)
            @@roman.each do |k,v|
                if num >= v
                    num -= v
                    ans << k
                    break
                end
            end
        end
        return ans.join
    end

    def to_s
        return "#{@original} : #{@roman_numeral} : #{@decimal} : #{@left_to_right}"
    end

end

def get_numbers_from_file(file)
    lines = []
    File.open(file) do |file|
        file.each_line do |line|
            lines << line.strip
        end
    end

    return lines
end

def main

    lines = get_numbers_from_file('roman.txt')

    diff = 0
    lines.each do |val| 
        rm = RomanNumeral.new(val)
        diff += rm.saved
    end
    puts diff

end

if __FILE__ == $0
    main
end


__END__

MMMMDXCV
1000 1000 1000 1000 500 10 100 5
