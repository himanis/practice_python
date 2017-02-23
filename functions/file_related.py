# file related functions
from collections import Counter
import random
fName = '/Users/himan/Documents/Himani-Data/Git-Working/practice_python/Config/user_name.txt'
fnum1 = '/Users/himan/Documents/Himani-Data/Git-Working/practice_python/Config/num1.txt'
fnum2= '/Users/himan/Documents/Himani-Data/Git-Working/practice_python/Config/num2.txt'
fname2 ='/Users/himan/Documents/Himani-Data/Git-Working/practice_python/Config/sowpos.txt'
def name_count_file():
    with open(fName) as names:
        nList = names.read().split("\n")
    for k in Counter(nList).iteritems():
        print k


def common_number_between_2_file():
    with open(fnum1,'r') as num1, open(fnum2,'r') as num2:
        nNum1 = num1.read().split("\n")
        nNum2 = num2.read().split("\n")
    lnew = [x for x in nNum1 if x in nNum2]
    print lnew
    return

def pick_word():
    with open(fname2) as dictory:
       rName = random.choice(dictory.readlines())
    print rName


class main():

    #name_count_file()
    #common_number_between_2_file()
    pick_word()

