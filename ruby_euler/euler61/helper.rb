

class Helper

    def self.triangle(n)
        return  n * (n + 1) / 2
    end

    def self.square(n)
        return n*n
    end

    def self.pentagonal(n)
        return n * (3 * n - 1) / 2
    end

    def self.hexagonal(n)
        return n * (2 * n - 1)
    end

    def self.heptagonal(n)
        return n * (5 * n - 3) / 2
    end

    def self.octagonal(n)
        return n * (3 * n - 2)
    end
    
end
