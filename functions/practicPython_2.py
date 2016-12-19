import sys
import random
import re
import string
from faker import Factory
import socket
import struct
from IPy import IP
import pdb
from netaddr.ip import IPAddress


class SmallFun():

    def __init__(self):
        print "I am constrctor"

    def getint(self):
        while True:
            numI = int(input("\n\tPlease enter a number "))
            if numI <= 0:
                print "Correct numeber".rjust(20)
                continue
            else:
                return numI

    def check_number_is_prime(self,c):
        while c != "n":
            num = self.getint()
            if (num%2 ==0 or num%3==0):
                print "Number is not prime".rjust(20)
            else:
                print "Number is prime".rjust(40)
            c = (raw_input("Continue (y/n)").rjust(20)).strip()
        return

    def sum_of_two(self,a,b):
        return a+b

    def Fibonacci(self):
        num = self.getint()
        if num ==1:
            F_list =[1]
        else:
            F_list =[1,1]
        for i in range(2,num):
            F_list.append(sum_of_two(F_list[i-2],F_list[i-1]))
        print F_list
        return

    """ REmove the duplicate from the list"""
    def remove_duplicate_in_list(self):
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

    def remove_duplicate_inlist_using_set(self):
        pdb.set_trace()
        l = [4, 23, 13, 35, 28, 5, 12, 12, 25, 15, 37, 15, 0, 14, 6, 10, 13, 36, 20]
        print "old list is" , l
        print "New list is" ,list(set(l))
        return

    def reverse_a_string_words(self):
        str1 = raw_input("string to reverse ")
        str1 = str1.split()
        str1.reverse()
        str1 = " ".join(str1)
        print str1
        return

    def reverse_a_string(self):
        str1 = raw_input(" Enter a string to reverse ")
        str2 =[]
        for i in range(len(str1) - 1, 0, -1):
            str2.append(str1[i])
        str1 = ''.join(i for i in str2)
        print str1
        return

# password genrations
    def passwd_gen(self):
        type= [string.uppercase,string.lowercase,string.digits,'~!@#$%^&*_?']
        pw = ''.join(random.choice(type[random.randint(0, 3)]) for i in range (16))
        print '{:5}{:<40}'.format("", pw)

        return

    def gen_ipaddree(self):
        print " \n first 5 ip's are created by faker"
        IP_addr = []
        fake = Factory.create()
        for i in range(4):
             IP_addr.append(fake.ipv4(network=False))

        print " next 5 ip is from socket"
        for i in range(5):
            IP_addr.append(socket.inet_ntoa(struct.pack('>I', random.randint(1,0xffffffff) ) ) )
        print " Next five are with simply join"
        for i in range(5):
             temp =".".join(str (random.randint(1,254) ) for i in range(4))
             IP_addr.append(temp)
        return IP_addr

    def gen_ipv6add(self):
        IPv6_addr = []
        M = 16 ** 4
        for i in range(5):
            IPv6_addr.append("2001:ca11:" + ":".join("%x" % random.randint(0, M) for i in range(6)))
        return

    def is_valid_IPv4_address(self,add):
         if add.count('.') == 3:
             try:
                 IP(add)
             except ValueError:
                 return False
         else:
             return False
         return True

    def is_ip_valid(self):
        print  "{:40}".format("Using gen_ipaddress to generate IPv4 and IPv5")
        ipList = self.gen_ipaddree()
        ipList.append('a.1.1.1')
        print ipList
        for i in ipList:
            if self.is_valid_IPv4_address(i):
                print "Vaild IP", i
            else:
                print "removeing", i
                ipList.remove(i)
        print ipList
        return






