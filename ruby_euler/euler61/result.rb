


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
    attr_accessor :path, :chain, :attempt

    def initialize(result=nil, id=nil)

        if id
           @chain = [id]
           @path  = [result] 
        else
           @chain = []
           @path  = [] 
        end

        @attempt = []
    end

    def check_chain()
        return ([0,1,2,3,4,5] - @chain).length == 0
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
        return ([0,1,2,3,4,5] - @attempt).length == 0
    end

    def add_attempt(in_val)
        @attempt << in_val
    end

    def rm_attempt(in_val)
        @attempt.delete(in_val)
    end

    def next_attempt
        z = @chain - @attempt
        return ([0,1,2,3,4,5] - z).first
    end
end
