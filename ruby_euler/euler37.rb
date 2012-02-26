#!/usr/bin/env ruby

$trunc = []
$primes = []
#truncatable primes
#

def better_sieve_upto(n)
  s = (0..n).to_a
  s[0] = s[1] = nil
  s.each do |p|
    next unless p
    break if p * p > n
    (p*p).step(n, p) { |m| s[m] = nil }
  end
  s.compact
end

=begin
def primeSieve(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    #can filter out all 200k's, 400's, 600's, 800's
    for i in range(2,9,2):
        candidates[i*100000:(i+1)*100000] = [None] * 100000
    return [i for i in candidates[2:] if i], candidates
=end

def is_prime(x)
  if x == 1
    return false
  end
  if x == 2
    return true
  end
  a = x ** 0.5
  2.upto(a) { |z|
    if x % z == 0
      return false
    end
  }
  return true
end

def is_trunc(y)
  1.upto(y.length-1) { |i|
    zz = y[i,y.length].to_i
    yy = y[0,y.length-i].to_i
    #if $primes.include?(zz) and $primes.include?(yy)
    #if x == 3797
    #end
    if is_prime(zz) and is_prime(yy)
      next
    else
      return false
    end
  }
  return true
end

$primes = better_sieve_upto(1_000_000)
puts $primes.length
$primes.delete(2)
$primes.delete(3)
$primes.delete(5)
$primes.delete(7)
#$primes.delete(11)
#$primes.delete(13)
#$primes.delete(17)
#$primes.delete(19)
$primes.each { |x|
  y = x.to_s
  next if y.start_with?('4') or y.start_with?('6') or y.start_with?(8) or y.start_with?('9')
  if is_trunc(y)
    puts x
    $trunc << x
    if $trunc.size == 11
      break
    end
  end
}

#(11..2_000_000).step(2) { |x|
#    if is_prime(x)
#      $primes << x
#      if is_trunc(x) 
#        puts x
#        $trunc << x
##puts x
##break
#      end
#    end
#    if $trunc.size == 10
#      break
#    end
#}

puts
puts $trunc
puts $trunc.reduce(:+)

