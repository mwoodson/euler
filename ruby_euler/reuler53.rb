#!/usr/bin/env ruby

require 'pp'

$scores = [
          "unknown" ,# =>  0
          "high"    ,# =>  1,
          "one"     ,# =>  2,
          "two"     ,# =>  3,
          "three"   ,# =>  4,
          "straight",# =>  5,
          "flush"   ,# =>  6,
          "full"    ,#=>   7,
          "four"    ,#=>   8,
          "sflush"  ,#=>   9,
          "royal"   ,#=>  10, 
         ]

class Card
    attr_accessor :suit, :value, :rank, :original
    def  initialize(card)
        @value, @suit = card.split(//)
        
        if @value =~ /A/i
            @rank = 14 
        elsif @value =~ /K/i
            @rank = 13 
        elsif @value =~ /Q/i
            @rank = 12 
        elsif @value =~ /J/i
            @rank = 11 
        elsif @value =~ /T/i
            @rank = 10 
        else
            @rank = @value.to_i
        end
        
        @original = card
    end

    def to_s
       puts "<PokerCard: #{@original}> #{@value} #{@suit} "
    end
end


def score_cards(cards)

    ranks = cards.collect { |c| c.rank } 
    #Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if cards.all? { |c| c.suit == cards[0].suit } &&
       cards.collect { |c| c.rank } - (10..14).to_a 
        return 10
    #Straight Flush: All cards are consecutive values of same suit.
    elsif cards.all? { |c| c.suit == cards[0].suit } &&
          0.upto(cards.length-2).collect { |ind| cards[ind+1].rank - cards[ind].rank == 1}.all?
        return 9
    #Four of a Kind: Four cards of the same value.
    elsif cards.any? { |c| ranks.count(c.rank) == 4 }
        return 8
    #Full House: Three of a kind and a pair.
    elsif cards.any? { |c| ranks.count(c.rank) == 3 } &&
          cards.any? { |c| ranks.count(c.rank) == 2 } 
        return 7
    #Flush: All cards of the same suit.
    elsif cards.all? { |c| c.suit == cards[0].suit }
        return 6
    #Straight: All cards are consecutive values.
    elsif 0.upto(cards.length - 2).collect { |ind| cards[ind+1].rank - cards[ind].rank == 1}.all?
        return 5
    #Three of a Kind: Three cards of the same value.
    elsif cards.any? { |c| ranks.count(c.rank) == 3 }
        return 4
    #Two Pairs: Two different pairs.
    elsif cards.any? { |c| ranks.count(c.rank) == 2 } &&
          ranks.uniq.length == 3
        return 3
    #One Pair: Two cards of the same value.
    elsif cards.any? { |c| ranks.count(c.rank) == 2 }
        return 2
    #High Card: Highest value card.
    else
        return 1
    end
end

class Hand
    attr_accessor :high, :pairs, :cards, :score
    def initialize(hand)
        @cards = hand.collect
        @score = score_cards(hand)
        ranks = @cards.collect { |c| c.rank } 
        if score == 1 #high card
            @high = ranks[-1]
        elsif score == 2#one pair
            @pairs = ranks.select { |r| ranks.count(r) ==  2 }.compact
            @high = pairs[-1]
        elsif score == 3#two pair
            @pairs = ranks.select { |r| ranks.count(r) ==  2 }.compact.sort
            @high = pairs[-1]
        elsif score == 4#three pair
            @high = ranks.select { |r| ranks.count(r) ==  3 }.compact
        elsif score == 5#straight
            @high = ranks[-1]
        elsif score == 6#flush
            @high = ranks[-1]
        elsif score == 7#full
            @pairs = ranks.select { |r| ranks.count(r) ==  2 }.compact
            @pairs << ranks.select { |r| ranks.count(r) ==  3 }.compact[0]
            @high = pairs[-1]
        elsif score == 8#four
            @pairs = ranks.select { |r| ranks.count(r) ==  4 }.compact.uniq
            @high = pairs[-1]
        elsif score == 9#sflush
            @high = ranks[-1]
        end
    end
end

def get_cards
    abort("Could not find poker.txt") unless File.exists?("poker.txt")
    
    player1 = []
    player2 = []

    File.foreach("poker.txt").each do |hand|
        cards = hand.split
        player1 += [cards[0,5].collect { |c| Card.new(c) }.sort { |a,b| a.rank <=> b.rank}]
        player2 += [cards[5,5].collect { |c| Card.new(c) }.sort { |a,b| a.rank <=> b.rank}]
    end

    return player1.zip(player2)
end

def main
    #player1 wins
    wins = 0

    #read in and prepare hands
    cards = get_cards
    
    cards.each do |hand|
        p1 = Hand.new(hand[0])
        p2 = Hand.new(hand[1])

#puts "Score: [#{$scores[p1.score]}] [#{$scores[p2.score]}]"
        if p1.score == p2.score
            if [2,3,4,7].include?(p1.score)
               comp = (p1.pairs.length - 1).downto(0).collect do |ind|
                    if p1.pairs[ind] > p2.pairs[ind]
                        true
                    elsif p1.pairs[ind] < p2.pairs[ind]
                        false
                    else 
                        nil
                    end
                end
                wins += 1 if comp.compact[0]
            elsif p1.high > p2.high
                wins += 1 
            end
        elsif p1.score > p2.score
            wins += 1
        end
    end
    puts "Player1: #{wins}"
end

if __FILE__ == $0
    main
end



__END__

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand            Player 1                Player 2                Winner
1               5H 5C 6S 7S KD
Pair of Fives
    2C 3S 8S 8D TD
Pair of Eights
    Player 2
2               5D 8C 9S JS AC
Highest card Ace
    2C 5C 7D 8S QH
Highest card Queen
    Player 1
3               2D 9C AS AH AC
Three Aces
    3D 6D 7D TD QD
Flush with Diamonds
    Player 2
4               4D 6S 9H QH QC
Pair of Queens
Highest card Nine
    3D 6D 7H QD QS
Pair of Queens
Highest card Seven
    Player 1
5               2H 2D 4C 4D 4S
Full House
With Three Fours
    3C 3D 3S 9S 9D
Full House
with Three Threes
    Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
