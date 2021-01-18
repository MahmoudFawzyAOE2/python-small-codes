print("u'll i/p 3 nums and o/p is the least")
while True :
    try :
        x = int (input("Enter number x "))
        y = int (input("Enter number y "))
        z = int (input("Enter number z "))
    except:
        print('\n re enter the numbers')
        continue
    break

if x<y and x<z :
    print('x is the least')
elif y<x and y<z :
    print('y is the least')
elif z<y and z<x :
    print('z is the least')
elif x==y==z :
    print('x & y & z are equal')
elif x==y :
    print('x & y are the least')
elif z==y :
    print('z & y are the least')
elif x==z :
    print('x & z are the least')
input ('Good bye :)')



