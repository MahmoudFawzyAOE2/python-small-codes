def up_tri (i,a,b):
    if i%2==0: #even
        l=int(i/2)
        for n in range(l):
            print ((l-n-1)*a+(2*(n+1))*b+(l-n-1)*a)
    else : #odd
        l=int((i+1)/2)+1
        for n in range(l):
            print ((l-n-1)*a+(2*(n-1)+1)*b +(l-n-1)*a)

def sides (i,a,b):
    l=int(i/2)
    for n in range(int(i/2.5)):
        print ((n)*a +b +(i-2-2*n)*a +b +(n)*a)

def base (i,a,b):
    if i%2==0: #even
        l=int(i/2)
        for n in range(int(2*i-2-2*int(2*i/2.5))-int(l/2),l-2,1):
            print ((l-n-1)*a+(2*(n+1))*b+(l-n-1)*a)
    else : #odd
        l=int((i+1)/2)+1
        for n in range(int(2*i-2-2*int(2*i/2.5))-int(l/3),l-2,1):
            print ((l-n-1)*a+(2*(n-1)+1)*b +(l-n-1)*a)


while True :
    x=int(input('Enter size: '))
    #y=input('Enter empty sides string: ')
    #z=input('Enter triangle filling string: ')
    up_tri(x,'  ','##')
    sides(2*x,' ','#')
    base (x,'  ','##')
    print('RAMADAN MUBARAK')
    #this code is has some small mistakes that causes only few imperfections but its main function is still working :)

    

