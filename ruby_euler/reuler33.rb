#!/home/kwoodson/.rvm/rubies/ruby-1.9.2-p180/bin/ruby
##!/usr/bin/env ruby
#
#
#
stime = Time.now
np = dp = 1
11.upto(99) { |n|
  (n+1).upto(99) { |d|
    next if n % 10 == 0 && d & 10 == 0
    a = n.to_s
    b = d.to_s
    if  a[0] == b[1] && a[1] < b[0]
      value = Float(a[1])/Float(b[0])
    elsif a[1] == b[0] && a[0] < b[1] 
      value = Float(a[0])/Float(b[1])
    else
      next
    end

    if (n.to_f / d.to_f == value)
      np *= n
      dp *= d
    end
  }
}
puts "#{dp}/#{np} => #{dp/np}"
puts "#{Time.now - stime}"
