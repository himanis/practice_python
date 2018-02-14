import sys
import pdb
from netaddr.ip import IPAddress
from collections import Counter

class Myline():

     def __init__(self,a,b):
         print a , "\t" , b
         self.c1 = a
         self.c2 = b
         return
     def dis(self):
        dist= ((self.c2[0]-self.c1[0])**2 + (self.c2[1]-self.c1[1])**2 )**0.5
        return dist

     def slope(self):
        s = float( (self.c2[0]-self.c1[0])/(self.c2[1]-self.c1[1]))
        return s
