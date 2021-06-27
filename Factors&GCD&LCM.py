
def factorize(num):   # function to have the prime factors of the given number
    pf=2              # initializing the prime factor (least prime factor is 2)
    factors=[]        # list to add all the factors in it
    while num!=1:     # if our number =1 , this means we reached the end
        mod=num%pf
        x = num/pf
        if mod == 0 : # mod = 0 means that this pf is one on the factors of the number. if not, go to the next pf
            factors.append(pf)
            num=x     # the new number takes place
        else :
            pf=pf+1   # go to the next pf (any non prime number {4,6,9,10,...} will cause no problem)
    return factors

def listmulti (lst): # simple loop to have the multiply of all the numbers inside a list
    multi = 1
    for num in lst :
        multi =  multi * num
    return multi

def GCD_LCM (n1,n2):
    f1= factorize(n1)
    f2= factorize(n2)

    if len(f1) > len(f2):              # just to begin the outer loop with the smaller list
        (f1,f2)=(f2,f1)                # f1 must be less than f2
    gcd_list=[]
    lcm_list=[]
    for c1 in range(len(f1)):
        for c2 in range(len(f2)):
            if f1[c1]==f2[c2] :        # if the 2 numbers are equal, this number belongs to gcd
                gcd_list.append(f2.pop(c2))
                break
            if c2 == len(f2)-1:        # if the element from first array doesn't match any from 2nd array , this number belongs to lcm
                lcm_list.append(f1[c1])
    lcm_list=gcd_list+lcm_list+f2                     # (gcd+lcm)=the first array , f2=unpoped elementes from 2nd array

    gcd_value = listmulti(gcd_list)
    lcm_value = listmulti(lcm_list)
    return (gcd_value,lcm_value)

############## the real start ############
num1=int(input('Enter first number:  '))
num2=int(input('Enter second number: '))

print('First  number prime factors are:',factorize(num1))
print('Second number prime factors are:',factorize(num2))

print('GCD:',GCD_LCM (num1,num2)[0])
print('LCM:',GCD_LCM (num1,num2)[1])
