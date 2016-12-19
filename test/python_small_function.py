import sys
sys.path.append('C:\\Users\\himan\\Documents\\Himani-Data\\Git-Working\\practice_python')
from functions.practicPython_2 import *

def display():
        print '{:5}{:<40}'.format("", "Please select the test to run")
        print '{:5}{:<40}'.format("", "q. Please select q to quit")
        print '{:5}{:<40}'.format("", "1. Find a prime number")
        print '{:5}{:<40}'.format("", "2. Fobanacci series")
        print '{:5}{:<40}'.format("", "3. remove the duplicate element in list")
        print '{:5}{:<40}'.format("", "4. remove the duplicate element using set")
        print '{:5}{:<40}'.format("", "5. reverse a string")
        print '{:5}{:<40}'.format("", "6. reverse_a_string_words")
        print '{:5}{:<40}'.format("", "7. check_ip_valid")
        print '{:5}{:<40}'.format("", "8. Generate IP's")
        print '{:5}{:<40}'.format("", "9. password Genration")
        return raw_input("please enter choice ")

def makechioce():
    choice = ''
    smallfun_inst = SmallFun()
    while choice.lower() != 'q':
        choice = display()
        if choice.lower() == 'q':
             break
        elif (choice == '1'):
            smallfun_inst.check_number_is_prime(choice)
        elif (choice == '2'):
            smallfun_inst.Fibonacci()
        elif (choice == '3'):
            smallfun_inst.remove_duplicate_in_list()
        elif (choice == '4'):
            smallfun_inst.remove_duplicate_inlist_using_set()
        elif (choice == '5'):
            smallfun_inst.string_in_reverse()
        elif (choice=='6'):
            smallfun_inst.reverse_a_string_words()
        elif(choice=='7'):
            smallfun_inst.is_ip_valid()
        elif(choice =='8'):
            IP_list = smallfun_inst.gen_ipaddree()
            print IP_list
        elif (choice == '9'):
            smallfun_inst.passwd_gen()
        else:
            print "wrong choice"
    return

if __name__== "__main__":
    makechioce()

