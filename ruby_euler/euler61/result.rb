


class Result

    attr_accessor :value, :first, :last, :id

    def initialize(num, id)
        @value = num
        z = num.to_s
        @first = z[0..1]
        @last  = z[-2..-1]
        @id = id
    end
end

class Chain
    attr_accessor :path, :chain

    def initialize(result=nil, id=nil)

        if id
           @chain = [id]
           @path  = [result] 
        else
           @chain = []
           @path  = [] 
        end
    end

    def next
        return ([0,1,2,3,4,5] - @chain).first
    end

    def rm_value
        @path.pop
        @chain.pop
    end

    def add_value(in_val)
        @path << in_val
        @chain << in_val.id
    end

    def done?
        0.upto(@path.size-1).each do |ind|
            if ind == @path.size - 1
                return false unless @path[ind].last == @path[0].first
            else
                return false unless @path[ind].last == @path[ind+1].first
            end
        end
        return ([0,1,2,3,4,5] - @chain).length == 0
    end

    def sum
        return path.inject(0) { |sum,z| sum + z.value }
    end
end
