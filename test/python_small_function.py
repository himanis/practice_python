import sys
sys.path.append('C:\\Users\\himan\\Documents\\Himani-Data\\Git-Working\\practice_python')
from functions.practicPython_2 import *

if __name__== "__main__":
    choice = ''
    smallfun_inst = SmallFun()
    while choice != 'q':
        print '{:5}{:<40}'.format("","Please select the test to run")
        print '{:5}{:<40}'.format("", "q. Please select q to quit")
        print '{:5}{:<40}'.format("","1. Find a prime number")
        print '{:5}{:<40}'.format("","2. Fobanacci series")
        print '{:5}{:<40}'.format("","3. remove the duplicate element in list")
        print '{:5}{:<40}'.format("","4. remove the duplicate element using set")
        print '{:5}{:<40}'.format("","5. reverse a string")
        print '{:5}{:<40}'.format("","6. password Genration")
        choice = raw_input("please enter choice ")
        if choice.lower() == 'q':
            break
        elif (choice == '1'):
            smallfun_inst.check_number_is_prime(choice)
            break
        elif (choice=='2'):
            smallfun_inst.Fibonacci()
            break
        elif (choice=='3'):
            smallfun_inst.remove_duplicate_in_list()
            break
        elif (choice=='4'):
            smallfun_inst.remove_duplicate_inlist_using_set()
            break
        elif (choice=='5'):
            smallfun_inst.string_in_reverse()
            break
        elif (choice=='6'):
            smallfun_inst.passwd_gen()
            break
        else:
            print "wrong choice"

