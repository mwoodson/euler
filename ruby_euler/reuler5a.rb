#!/usr/bin/env ruby
#
#
#20, 19, 18, 17, 16, 15, 14, 13, 12, 11
#a=(11..19).step(2).to_a
#b=(12..20).step(2).to_a
nums = [19, 13, 11, 17, 18, 16, 15, 14, 12 ]
#nums = 10.downto(1).to_a
#nums = 20.downto(11).to_a
#nums = (11..20).to_a

(2520..300000000).step(2520) { |x|
#(1_000_000..300_000_000).step(2520) { |x| 
# nums.each { |y|
#   if x % y != 0 
#     break
#   end
#   if y == nums.last
#     puts x
#     abort('Found it!')
#   end
# }

if nums.any? {|j| x % j != 0 }
next
else
puts x
abort("Found it.")
end
}
abort('Not Found')



#create a list of each
#then take set differences
