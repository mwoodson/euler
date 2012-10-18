#!/usr/bin/ruby
#
#
num_sum = 0

#for (i=0; i<1000;i++)
for i in 1..1000
    if i % 3 == 0 || i % 5 == 0
        num_sum += i
    end
end    

print "#{num_sum}\n"
