#!/usr/bin/env python
#import pdb


#coins = [200, 100, 50, 20, 10, 5, 1]
#coins = [10, 5, 2, 1]
#rcoins = coins[::-1]
#amount = 10
#count = 0

def partitions(amnt):
    if amnt == 0:
        yield []
        return
    for p in partitions(amnt-1):
        yield[1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            #pdb.set_trace()
            yield [p[0] + 1] + p[1:]

#def comb_change(amnt):
#    pass
#    

#'''
#Just type it in here
#on the 20 coin, line 3:
#v=value of coin associated with column
#r=row
#
#c0      c1              c2                      c3              c4
#        amount / v(c1)  0                       0               0 
#0	2	        0	                0	        0
#
#        prev row - 1    amt - v(c1) / v(c2)     amt - v(c1) + v(c2) / v(c3)
#0	1	        2       	        0	        0
#
#
#IDEA #2
#1               2               5               10              20
#amount          0               0               0               0
#amount - 1v(c2) 1               0               0               0
#amount - 2v(c2) 2               0               0               0
#amount - 3v(c2) 3               0               0               0
#...
#...
#amount - v(c5)  0                1               0               0
#amount - v(c5) 0                1               0               0
#0	1	1	0	5
#0	1	0	5	0
#0	1	0	4	2
#0	1	0	3	4
#0	1	0	2	6
#0	1	0	1	8
#0	1	0	0	10
#0	0	4	0	0
#0	0	3	2	1
#0	0	3	1	3
#0	0	3	0	5
#0	0	2	5	0
#0	0	2	4	2
#0	0	2	3	4
#0	0	2	2	6
#0	0	2	1	8
#0	0	2	0	10
#0	0	1	7	1
#0	0	1	6	3
#0	0	1	5	5
#0	0	1	4	7
#0	0	1	3	9
#0	0	1	2	11
#0	0	1	1	13
#0	0	1	0	15 #special case here because we have 0 in the middle
#ones hit 0 or current coin has no remainder, we need to borrow again
#0	0	0	10	0
#0	0	0	9	2
#0	0	0	8	4
#0	0	0	7	6
#0	0	0	6	8
#0	0	0	5	10
#0	0	0	4	12
#0	0	0	3	14
#0	0	0	2	16
#increment counter for 5's if we hit amnt then we need to borrow else count 1's
#0	0	0	1	18 
#hit 20 here so then we need to borrow.  then count til we hit amount
#0	0	0	0	20 go as far as you can then borrow
#count ones up until we hit the amount or if we are >= 1
#'''
def hope_it_works2(amnt):
    count = 0
    #print "AMNT="+str(amnt)
    for ind200 in range(0,200,1):
        tmp_amnt_200 = amnt - (ind200 * 200)
        for ind100 in range(0,tmp_amnt_200,1):
            tmp_amnt_100 = tmp_amnt_200 - (ind100 * 100)
            if tmp_amnt_100 > 0:
                for ind50 in range(0,tmp_amnt_100,1):
                    tmp_amnt_50 = tmp_amnt_100 - (ind50 * 50)
                    if tmp_amnt_50 > 0:
                        for ind20 in range(0,tmp_amnt_50,1):
                            tmp_amnt_20 = tmp_amnt_50 - (ind20 * 20)
                            if tmp_amnt_20 > 0:
                                for ind10 in range(0,tmp_amnt_20,1):
                                    tmp_amnt_10 = tmp_amnt_20 - (ind10 * 10)
                                    if tmp_amnt_10 > 0:
                                        for ind5 in range(0,tmp_amnt_10,1):
                                            tmp_amnt_5 = tmp_amnt_10 - (ind5 * 5)
                                            if tmp_amnt_5 > 0:
                                                for ind2 in range(0,tmp_amnt_5,1):
                                                    tmp_amnt_2 = tmp_amnt_5 - (ind2 * 2)
                                                    #if tmp_amnt_2<=0:# or tmp_amnt_5 <= 0:
                                                        #break
                                                    b = tmp_amnt_5 - (ind2 * 2)
                                                    #print [x for x in [ind200, ind100, ind50, ind20, ind10, ind5, ind2, b]]
                                                    yield [x for x in [ind200, ind100, ind50, ind20, ind10, ind5, ind2, b]]
                                                    count += 1  
                                                    if tmp_amnt_5 - ((ind2+1) * 2) < 0:
                                                        break
                                            if tmp_amnt_5 == 0:
                                                #print [x for x in [ind200, ind100, ind50, ind20, ind10, ind5,0 , 0]]
                                                yield [x for x in [ind200, ind100, ind50, ind20, ind10, ind5,0 , 0]]
                                                count += 1  
                                            if tmp_amnt_5 < 0:
                                                break
                                    if tmp_amnt_10 == 0:
                                        #print [x for x in [ind200, ind100, ind50, ind20, ind10, 0,0 , 0]]
                                        yield [x for x in [ind200, ind100, ind50, ind20, ind10, 0,0 , 0]]
                                        count += 1  
                                    if tmp_amnt_10 < 0:
                                        break
                            if tmp_amnt_20 == 0:
                                #print [x for x in [ind200, ind100, ind50, ind20, 0, 0,0 , 0]]
                                yield [x for x in [ind200, ind100, ind50, ind20, 0, 0,0 , 0]]
                                count += 1  
                            if tmp_amnt_20 < 0:
                                break
                    if tmp_amnt_50 == 0:
                        #print [x for x in [ind200, ind100, ind50, 0, 0, 0,0 , 0]]
                        yield [x for x in [ind200, ind100, ind50, 0, 0, 0,0 , 0]]
                        count += 1  
                    if tmp_amnt_50 < 0:
                        break
            if tmp_amnt_100 == 0:
                #print [x for x in [ind200, ind100, 0, 0, 0, 0,0 , 0]]
                yield [x for x in [ind200, ind100, 0, 0, 0, 0,0 , 0]]
                count += 1  
            if tmp_amnt_100 < 0:
                break
        if tmp_amnt_200 == 0:
            #print [x for x in [ind200, 0, 0, 0, 0, 0,0 , 0]]
            yield [x for x in [ind200, 0, 0, 0, 0, 0,0 , 0]]
            count += 1  
        if tmp_amnt_200 < 0:
            break
#return count

#def hope_it_works(amnt,rcoins):
#    count = 0# of solutins
#    ind = 0#index into coins
#
#    twos_amnt=0
#    tmp_amnt = amnt
#    one = 0
#    two = 0
#    five = 0
#    ten = 0
#    twenty = 0
#    fifty = 0
#    one_hund = 0
#    two_hund = 0
#    while(fifty * 50 < amnt):
#        tmp_amnt_50 = amnt - (twenty * 20)
#        while(twenty * 20 < amnt):
#            tmp_amnt_20 = tmp_amnt_50 - (twenty * 20)
#            while(ten * 10 < amnt):
#                tmp_amnt_10 = tmp_amnt_20 - (ten * 10)
#                while(five * 5 < tmp_amnt_10):
#                    tmp_amnt_5 = tmp_amnt_10 - (five * 5)
#                    b = tmp_amnt_5
#                    while(two * 2 < tmp_amnt_5):#for two in range(200):
#                        if b <= 0 or tmp_amnt_5-(two*2) < 0:
#                            print "fifties: %s\t\ttwenties: %s\t\ttens: %s\t\tfives: %s\t\ttwos: %s\t\tones: %s "%(fifty,twenty,ten,five,two,b)
#                            count += 1
#                            break
#                        else:
#                            b = tmp_amnt_5 - (two * 2)
#                            print "fifties: %s\t\ttwenties: %s\t\ttens: %s\t\tfives: %s\t\ttwos: %s\t\tones: %s "%(fifty,twenty,ten,five,two,b)
#                            count += 1
#                        two += 1
#                    if tmp_amnt_5-(two*2)>=0:
#                        print "fifties: %s\t\ttwenties: %s\t\ttens: %s\t\tfives: %s\t\ttwos: %s\t\tones: %s "%(fifty,twenty,ten,five,two,0)
#                        count += 1
#                    five+=1
#                    two = 0
#                if (five*5 >= tmp_amnt_5) or tmp_amnt_5 >= 5:
#                    print "fifties: %s\t\ttwenties: %s\t\ttens: %s\t\tfives: %s\t\ttwos: %s\t\tones: %s "%(fifty,twenty,ten,five,0,0)
#                    count += 1
#                ten += 1
#                five= 0
#                two = 0
#            if (ten*10 - tmp_amnt_10 <= 0 or tmp_amnt_10 >= 10):
#                print "fifties: %s\t\ttwenties: %s\t\ttens: %s\t\tfives: %s\t\ttwos: %s\t\tones: %s "%(fifty,twenty,ten,0,0,0)
#                count += 1
#            twenty+=1
#            ten = 0
#            five= 0
#            two = 0
#            if (twenty*20 - tmp_amnt_20 <= 0 or tmp_amnt_20 >= 20):
#                print "fifties: %s\t\ttwenties: %s\t\ttens: %s\t\tfives: %s\t\ttwos: %s\t\tones: %s "%(fifty,twenty,0,0,0,0)
#                count += 1
#        fifty+=1
#        twenty=0
#        ten = 0
#        five= 0
#        two = 0
#        if (fifty*50 - tmp_amnt_50 <= 0 or tmp_amnt_50 >= 50):
#            print "fifties: %s\t\ttwenties: %s\t\ttens: %s\t\tfives: %s\t\ttwos: %s\t\tones: %s "%(fifty,0,0,0,0,0)
#            count += 1
#    return count
#'''
#0 0 0 20
#0 0 1 18
#0 0 2 16
#'''
#def test(x):
#    count = 0
#    sols = partitions(x)
#
#    for sol in sols:
#        for z in sol:
#            if z not in [200,100,50,20,10,5,2,1]:
#                break
#        else:
#            count += 1
#            #print sol
#    return count
if __name__ == "__main__":
    print hope_it_works2(200)
#print len([x for x in partitions(200)])
#for i in range(1,26):
#    h = hope_it_works(i,rcoins) 
#    t = test(i)
#    if hope_it_works(i,rcoins) == test(i):
#        print str(i) + ": PASS"
#    else:
#        print str(i) + ": FAIL h ="+str(h)+" t="+str(t)
#    break
#print hope_it_works(i,rcoins)




#num_times, remainder = divmod(amnt,c)
#            if num_times == amnt and remainder == 0:#redundant but might need remainder later
#                #first time should be 20 pennies
#                #a dead match so we need to borrow
#                ind += 1
#                #found a solution
#                count += 1
#                break#go borrow the next coin
#problem now is the divmod so maybe we don't want that cause on 2nd loop the divmod will be 10, 0 which we only want 1
        





