while True :

        #we use try/except to detect input to be intger not string 
        try :
            num =int(input('Enter intger (from 0 to 9) ')) 
        except :
            print('\nWrong input! :(\nmust enter a number')
            continue
        
        #we use if condition to detect input within a certain range
        if num>9 or num<0 :
            print('\nWrong input! :(\nmust enter a number (from 0 to 9)')
            continue
        
        #the loop will break only when there is no error in try/except and the num within the certain range
        break
