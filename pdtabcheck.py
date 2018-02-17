def simulatetourney(arr1,roundnumber):
    #arr1 is team count
    import random
    arr1=int(arr1)
    scores=[0 for i in range(int(arr1))]
    roundnumber=int(roundnumber)
    newarray=[]

    def match(array,newarray,roundnumber):
        a = array[-2:] #simulating top matchup
        for i in a:
            array.remove(i) #removing those elements from list
        #print(a)
        winner=random.randint(0, 1)#random winner
        a[winner] = a[winner] + 1

        for i in a:
            newarray.append(i) #adding to new list after assigning win
        if(array):
            #print(array)
            array, newarray, roundnumber=match(array,newarray,roundnumber)
        else:
            #print('els')
            roundnumber=roundnumber+1
        return(array,newarray,roundnumber)

    #print(scores,newarray,roundnumber)
    newarray.sort()
    scores.sort()
    scores,newarray,roundnumber=match(scores,newarray,roundnumber)
    newarray.sort()
    scores.sort()
    for i in range(roundnumber-2):
        #print('Round'+str(i))
        scores=newarray
        newarray=[]
        scores, newarray, roundnumber=match(scores,newarray,roundnumber)
        newarray.sort()
        scores.sort()

    newarray.sort()
    afteriteration1=newarray
    #print(str(afteriteration1))
    #print(sum(afteriteration1))
    return (afteriteration1)

list=[]

roundcount=input('Enter rounds: ')
teamcount=input('Enter teamcount: ')


teamcount = int(teamcount)
if ((teamcount) % 2 == 1):
    teamcount = (teamcount) + 1
    print('ODD number bc, I\'m adding a swing')

for i in range(500):
    a=simulatetourney(teamcount,roundcount)
    if not a in list:
        list.append(a)

print('All possible results:')
print(list) #all possible results
breakcount=input('enter number of breaking teams: ')
breakcount=int(breakcount)
if breakcount>teamcount:
    print('Dont be chuu')
    exit()

list=[i[::-1][0:breakcount-1] for i in list]
print('Breaking teams:')
print(list) #breaking teams