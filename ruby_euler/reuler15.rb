#!/usr/bin/env ruby

require 'pp'

=begin
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

Combination formula states:
for a 4x3 rectangle
possible solutions is C(n,r) = n! / (r! * (n-r)!
7 steps to find a solution 
so:
    C(7,4) = 7! / (4! * (7-4)!

so for 20x20 grid
possible combinations = C(40,20) = 40!/ (20! * (40-20)!
    fact(40) / (fact(20) * fact(40-20))
    137846528820L

def fact(x): 
    return (1 if x==0 else x * fact(x-1))
=end
#order does not matter

#print fact(40)/(fact(20) * fact(40-20))
#MAX_MOVES = 3 #2x2 grid, moves = 4 but zero based is 3
#MAX_MOVES = 5 #2x2 grid, moves = 4 but zero based is 3
#MAX_MOVES = 40 #2x2 grid, moves = 4 but zero based is 3
MAX_MOVES = 10 #2x2 grid, moves = 4 but zero based is 3
#MAX_ROWS = 20 #2x2 grid, moves = 4 but zero based is 3
MAX_ROWS = 5 #2x2 grid, moves = 4 but zero based is 3
rows = []
(0...MAX_ROWS+1).each do |x|
  if x == 0
    rows <<  [1] * (MAX_ROWS+1)
  else
    rows <<  [0] * (MAX_ROWS+1)
  end
end

=begin
0.upto(MAX_ROWS-1).each do |x|
    rows[MAX_ROWS][x] = 1
    rows[x][MAX_ROWS] = 1
end
=end
#rows[0][0] = 1
0.upto(MAX_ROWS).each do |x|
    rows[x][0] = 1
end

pp rows


#=begin
1.upto(MAX_ROWS) do |x|
    1.upto(MAX_ROWS) do |y|
        rows[x][y] += rows[x][y-1] + rows[x-1][y] #to the left and above
    end
end
puts "ANS=#{rows[MAX_ROWS][MAX_ROWS]}"
#sum += rows[x].inject(:+)
#rows.each do |r|
#pp r
#end
#=end

=begin
(MAX_ROWS - 1).downto(0).each do |i|
    puts "i=#{i}"
    (MAX_ROWS - 1).downto(0).each do |j|
        puts "j=#{j}"
        puts "HERE"
        rows[i][j] = rows[i][j+1] + rows[i+1][j] #to the left and above
    end
end
=end

#puts rows[0][0]
rows.each do |r|
pp r
end


#puts sum+MAX_ROWS+1

__END__
#counter=0
#def doPath(x, y, MAX):
#    global counter
#    if (x==MAX and y==MAX):
#        counter+=1
#        return
#    elif (x > MAX or y > MAX):
#        return
#    doPath(x+1,y, MAX)
#    doPath(x,y+1, MAX)
#
#doPath(0,0, 20)
#print counter
#size_of_grid = 20
#alist = []


