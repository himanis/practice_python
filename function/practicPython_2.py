import sys
import random
import re
import string
from faker import Factory
import socket
import struct
from IPy import IP

def getint():
    while True:
     numI = int(input("\n\tPlease enter a number "))
     if numI <= 0:
         print "Correct numeber".rjust(20)
         continue
     else:
        return numI

def make_a_choice(a):
    return{
        '1':check_number_is_prime()
    }.get(a,'q')


def check_number_is_prime(c):
    while c!="n":
        num = getint()
        if (num%2 ==0 or num%3==0):
            print "Number is not prime".rjust(20)
        else:
            print "Number is prime".rjust(40)
        c = raw_input("Continue (y/n)").rjust(20)
        return
def sum_of_two(a,b):
    return a+b
def Fibonacci():
    num = getint()
    if num ==1:
        F_list =[1]
    else:
        F_list =[1,1]
        for i in range(2,num):
            F_list.append(sum_of_two(F_list[i-2],F_list[i-1]))
    print F_list
    return

""" REmove the duplicate from the list"""

def remove_duplicate_in_list():
    #l= random.sample(range(30),random.randint(20,30))
    l =[4, 23, 13, 35, 28, 5, 12, 12, 25, 15, 37, 15, 0, 14, 6, 10, 13, 36, 20]
    lnew = []
    print " Creating a list from random numbers".rjust(20)
    print l
    for ele in l:
        if (ele in lnew):
            print "\n duplicate one",ele
            continue
        else:
            lnew.append(ele)
    print lnew
    return
def remove_duplicate_inlist_using_set():
    l = [4, 23, 13, 35, 28, 5, 12, 12, 25, 15, 37, 15, 0, 14, 6, 10, 13, 36, 20]
    print "old list is" , l
    print "New list is" ,list(set(l))
    return

def string_in_reverse():
    str1 = raw_input("string to reverse")
    str1 = str1.split()
    str1.reverse()
    str1 = " ".join(str1)
    print str1
    return

# password genrations
def passwd_gen():
    type= [string.uppercase,string.lowercase,string.digits,'~!@#$%^&*_?']
    pw = ''.join(random.choice(type[random.randint(0, 3)]) for i in range (16))
    print '{:5}{:<40}'.format("", pw)
    return

def gen_ipaddree():
    print " \n first 5 ip's are created by faker"
    fake = Factory.create()
    for i in range(4):
        print fake.ipv4(network=False)
    print " next 5 ip is from socket"
    for i in range(5):
        print socket.inet_ntoa(struct.pack('>I', random.randint(1,0xffffffff)))
    print " Next five are with simply join"
    print ".".join(str (random.randint(1,254) ) for i in range(4))
    return




