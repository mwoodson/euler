#!/usr/bin/ruby
#  The prime factors of 13195 are 5, 7, 13 and 29.
#
#  What is the largest prime factor of the number 600851475143 ?
#
#
def sieve_gen(num)
    primes = (1..Math.sqrt(num)).to_a

    for i in [2,3,5,7]
        tnum = 0
        begin
            tnum += i
            primes[tnum] = nil
        end until tnum >= Math.sqrt(num)
    end
    return primes.drop_while { |x| x == nil }
#return primes.delete_if {[i] i == nil}
end


def isprime(x)
    if x == 1 || x == 2
        return true
    end
    for i in 3..Math.sqrt(x)
        if x % i == 0
            return false
        end
    end
    return true
end

num = 600851475143
#num = 13195
primes = sieve_gen(num)
for i in primes
    if i > Math.sqrt(num)
        break
    end
    if num % i == 0
        puts i
    end
end
#print primes
__END__
for i in 1.step(Math.sqrt(num), 2)
    if isprime(i) && num % i == 0
        puts i
#primes << i
    end
end

#puts primes[-1]
