print('\t\t\t\t\tWelcome to Indian Bank ATM')
restart=('Y')
chances = 3
pin1 = 1234
pin2 = 5678
users=['1','2']
pins=[pin1,pin2]
userid=input('\t\tEnter User ID: ')
if userid==users[0] or userid==users[1]:
    while chances >= 0:
        pin=0
        pin = int(input('\tPlease Enter Your 4 Digit Pin: '))
        if pin==pins[0]:
            user=users[0]
            print('Welcome:SATHISH',userid)
            balance=240000.74
            print('You entered your pin Correctly\n')
            a=1
        elif pin==pins[1]:
            user=users[1]
            print('Welcome:PAVITHRA',userid)
            balance=550000.45
            print('You entered your pin Correctly\n')
            a=1
        else:
            print('\t\t\t\t\tIncorrect Password')
            a=0
            chances = chances - 1
            if chances == 0:
                print("\n\t\t\tSORRY !!\n\t\t   No more tries!!!")
                break
        if a==1:

            while restart not in ('n','NO','no','N'):
                print('Press 1\t To Check Your Balance\n')
                print('Press 2\t To Make a Withdrawal\n')
                print('Press 3\t To Deposit\n')
                print('Press 4\t To Change Your ATM Pin\n')
                print('Press 5\t To Return Card\n')
                option = int(input('What Would you like to choose?'))
                if option == 1:
                    print('Your Balance is Rs.',balance,'\n')
                    restart = input('Would You like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif option == 2:
                    option2 = ('y')
                    withdrawl = float(input('How Much Would you like \nRs50/Rs100/Rs200/Rs500/Rs2000/Rs3000 for other enter 1: '))
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Rs',balance)
                    restart = input('Would You like to go back? ') 
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                    restart = ('y')
                elif option == 3:
                    Pay_in = float(input('How Much Would You Like To Pay In? '))
                    balance = balance + Pay_in
                    print ('\nYour Balance is now Rs',balance)
                    restart = input('Would You like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif option == 5:
                    print('Please wait while your card is Returned...\n')
                    print('\t\t\t\t\tThank you for banking with us !!!')
                    break
                elif option == 4:
                    cpin=int(input('Enter Your Current Pin:'))
                    if cpin==pins[0]:
                        npin=int(input('Enter Your New Pin:'))
                        conpin=int(input('Confirm Your New Pin:'))
                        if npin!=conpin:
                            print('\t\t\t\t\tPin Has Been Not Matched!!!')
                        else:
                            print('\t\t\t\t\tPin Has Been Changed Successfully!!!')
                            pins[0]=conpin
                    elif cpin==pins[1]:
                        npin=int(input('Enter Your New Pin:'))
                        conpin=int(input('Confirm Your New Pin:'))
                        if npin!=conpin:
                            print('\t\t\t\t\tPin Has Been Not Matched!!!')
                        else:
                            print('\t\t\t\t\tPin Has Been Changed Successfully!!!')
                            pins[1]=conpin
                    else:
                        print('\t Incorrect Pin')
                    break

                else:
                    print('Please Enter a correct number. \n')
                    restart = ('y')
        
            
