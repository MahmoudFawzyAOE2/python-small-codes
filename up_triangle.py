def up_tri (i,a,b):
    if i%2==0: #even
        l=int(i/2)
        for n in range(l):
            print ((l-n-1)*a+(2*(n+1))*b+(l-n-1)*a)
    else : #odd
        l=int((i+1)/2)+1
        for n in range(l):
            print ((l-n-1)*a+(2*(n-1)+1)*b +(l-n-1)*a)

while True :
    x=int(input('Enter size: '))
    y=input('Enter empty sides string: ')
    z=input('Enter triangle filling string: ')
    up_tri(x,y,z)

    

