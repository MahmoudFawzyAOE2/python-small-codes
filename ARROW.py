def pos_tri (x,d):
    n=0
    for n in range(x) :
        if d==0:
            print ((x*2)*'# '+(x*2)*'# '+(x*2)*'# '+(n+1)*'# ')
        else:
            print ((x*2+1)*'# '+(x*2+1)*'# '+(x*2+1)*'# '+(n+1)*'# ')
def neg_tri (x,d):
    n=0
    for n in range(x) :
        if d==0:
            print ((x*2)*'# '+(x*2)*'# '+(x*2)*'# '+(x-n)*'# ')
        else:
            print ((x*2+1)*'# '+(x*2+1)*'# '+(x*2+1)*'# '+(x-n)*'# ')
        
    
x=int(input('enter the size: '))
n=0

#Upper half
for n in range(x) :
    print (x*'# '+x*'  '+(n+1)*'# ')

#Middle Half
if x%2==0: #even
    v=int(x/2)
    pos_tri(v,0)
    neg_tri(v,0)
else : #odd
    v=int((x-1)/2)
    pos_tri(v,1)
    print (x*'# '+x*'# '+x*'# '+int((x+1)/2)*'# ')
    neg_tri(v,1)

#Lower Half
for n in range(x) :
    print (x*'# '+x*'  '+(x-n)*'# ')    
    

