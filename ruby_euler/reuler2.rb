#!/usr/bin/ruby
#
#
def fib(x)
    if x == 0
       return 0
    elsif x == 1
       return 1
    end
    return fib(x-1) + fib(x-2)
end
#for (i=0; i<1000;i++)
#for( i=2; i < 4000000; i+=2)
num_sum = 0
for i in 1..1000000
    z = fib(i)
    if z > 4000000
        break
    end
    if z % 2 == 0
       num_sum += z
    end
end

print "#{num_sum}\n"

