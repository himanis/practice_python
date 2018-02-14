from collections import OrderedDict
from collections import Counter
import operator


d = {'a': 100, 'b': 200, 'x':90, 'c':300, 'd':50 , 'f':900, 'e':34}
bdayd= {
    'abc':'12/3/1961',
    'b':'12/4/1962'
}


def order_dict():
    print " orignal dict ", d ,"\n"
    print " The sorted on Values " , sorted(d.items(),key= lambda x:x[1])
    print " The Reversed  on Values", sorted(d.items(), key=lambda x: x[1], reverse= True)
    print "\n"
    print " The sorted on Items", sorted(d.items(), key=lambda x: x[0])
    print " The Reversed  on Items", sorted(d.items(), key=lambda x: x[0], reverse=True)

    print " from OrderDict"
    print OrderedDict(d)

def map_dict():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    newd = dict()
    for d1 in (dic1, dic2, dic3):
        newd.update(d1)
    print newd

    print " short dic by key"
    print sorted(d.items(),key=lambda x:x[0])

    print " find min and max in directory by values"
    l = sorted(d.items(), key= lambda x:x[1])
    print " Mix key and item", l[0][0], l[0][1]
    print " Max key and item", l[-1][0], l[-1][1]

def add_values_of_two_list():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    dn = dict()
    '''for k in d1.iterkeys():
        if k in d2.keys():
            dn[k]=d1[k]+d2[k]
        else:
            dn[k]=d1[k]
    for k in d2.iterkeys():
        if k not in d2.keys():
            dn[k] =d2[k]
    print dn'''

    dn = Counter(d1)+Counter(d2)
    print dn

    print " Print unique values in the list "
    sdata=  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    newlist = set(val for L in sdata for val in L.values())
    print newlist

    print " First 3 higest values in dict"  , d
    print sorted(d.values(), reverse=True)[:3]

    print " create dict from string",
    print Counter("stringing")

    dlist =[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    print "Make a Directory form list", dlist
    newd = dict()
    for i in dlist:
        l = i.values()
        newd[l[0]]=l[1]
    print newd ,"\n"

    print " Add two list to make  a dict"
    newd.clear()
    l1 =['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
    l2= [1, 2, 2, 3]
    for ele in zip(l1,l2):
        newd[ele[0]] =ele[1]
    print newd

    print "\n convert directory ot ordered dict", newd
    newdd = OrderedDict(newd)
    print newdd


def find_the_key_dic():
    print " welcome to the brithday diary, we know bday of"
    for k in bdayd:
        print k
    bkey = raw_input(" You want to know the bday of ")
    bkey= bkey.strip()
    print bdayd[bkey]

    return


def sum67(num):
    sum1, i = 0, 0

    while (i < len(num)):
        if num[i] != 6:
            sum1 = sum1 + num[i]
            i = i + 1
            print "in non6 loop" , i, num[i], sum1
        else:
            while (i < len(num)):
                print i, num[i],sum1
                if num[i]!=7:
                    i = i + 1
                else:
                    i=i+1
                    break
    print  sum1

def has22(nums):
  for i in range(len(nums)):
      if nums[i]==2 and nums[i+1]==2:
          return True
  return False


def centered_average(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) > 2:
        nums = nums[1:-1]
    return sum(nums) / len(nums)





class main():
    #order_dict()
    #map_dict()
    #add_values_of_two_list()
    #find_the_key_dic()
    #sum67([1, 2, 2])
    #print  has22([1, 2, 1,2,3,2,2])
    print centered_average([1, 1, 5, 5, 10, 8, 7])

