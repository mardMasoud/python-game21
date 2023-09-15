import random
khal = ['geshniz','del','khesht','pik']
rank = ['2','3','4','5','6','7','8','9','10','sarbaz','bibi','king','us']
dast=[]
for i in rank:
    for j in khal:
 

       dast.append(i+' of '+j)

d=[]
for i in range(21):
    x=random.choice(dast)
    d.append(x)
    dast.remove(x)
print(d)
print('--------------------------------------')
input('please a card')
print('--------------------------------------')
for i in range(3):
    d1=d[:19:3]
    d2=d[1:20:3]
    d3=d[2:21:3]
    print('dast 1:',d1)
    print('--------------------------------------')
    print('dast 2:',d2)
    print('--------------------------------------')
    print('dast 3:',d3)
    print('--------------------------------------')
    x = input('please a dast: ')
    if int(x)==1:
        d=d3+d1+d2
        print('--------------------------------------',x)

        print(d)
        print('--------------------------------------',x)

    elif int(x)==2:
        d=d3+d2+d1
        print('--------------------------------------',x)

        print(d)
        print('--------------------------------------')
        
    elif int(x)==3:
        d=d1+d3+d2
        print('--------------------------------------')

        print(d)
        print('--------------------------------------')
                

print('-------------------------')
print('Your Card: ',d[10])




