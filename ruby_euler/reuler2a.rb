#!/usr/bin/ruby
#Dynamic Programming Version
#nums = { 1 => 1, 2 => 1  }
nums = [0, 1, 1]
num_sum = 0
for i in 3..1000000
    z = nums[i-1] + nums[i-2]
    if z > 4000000
        break
    end
    if z % 2 == 0
       num_sum += z
    end
    nums[i] = z
end

print "#{num_sum}\n"
__END__
0 = 0
1 = 1
2 = 1
3 = 2
4 = 3
5 = 5
6 = 8
7 = 13

