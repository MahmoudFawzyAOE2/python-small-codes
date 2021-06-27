print('guess a number between 0 & 100')
input('click Enter to start :) ')

g=0
high = 100
low = 0
med =50
while g!=med :
    print('\n Is your number equal {} ?'.format(med))
    g=input('Enter "h" for (higher), "l" for (lower), "e" for (equal) >> ')
    if g== 'h' :
        low = med
        med = (high+low)//2
    elif g=='l':
        high = med
        med = (high+low)//2
    else :
        g= med

print('\n your number is',g)
input('good bye :) ')
