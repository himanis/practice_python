import sys
sys.path.append('C:\\Users\\himan\\Documents\\Himani-Data\\Git-Working\\practice_python')
from functions.line_Cyl import *

def play():
       C1 = (10,20)
       C2 = (30,40)
       li =Myline(C1,C2)
       print "distance ", li.dis()
       print "slop is" , li.slope()



class __main__():
    play()
