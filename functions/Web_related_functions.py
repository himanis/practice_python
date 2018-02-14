import struct
import string
import re
import random
import requests
import urllib
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json
import socket
import httplib
import Config




file_xml ='C:\Users\himan\Documents\Himani-Data\Git-Working\practice_python\Config\\book2.xml'
file_json='C:\\Users\\himan\\Documents\\Himani-Data\\Git-Working\\practice_python\\Config\\facebook.json'

class WebFun():
    def __init__(self):
        return

    def list_articles_on_NYT(self,base_url):
        print "\n\t The list of the articles on the New Yoke Time"
        r = requests.get(base_url)
        soup = BeautifulSoup(r.text,'html.parser')
        '''we can usr urllib also
        html = urllib.urlopen(base_url).read()
        soup = BeautifulSoup(html,'html.parser')
        '''
        '''
         There are two type of headings h2 and h3, where h2 has a inbuild herf  OR h2 has another heading such as h3 but no external link
        We are going to treat them differently.
        Check if we have 'a' then get the text otherwise just get the contains.
        </h2>
        <h2 class="story-heading">
        <a href="  "  </a>

        </h2>
        <h3 class="story-heading">
        something
        </h3>
        '''
        for link in soup.find_all(class_="story-heading"):
            if link.a:
                print "EXTERNAL_LINK:", '{:<40}'.format(link.a.text.replace("\n",'').strip().encode('utf-8'))
            else:
                print '{:<40}'.format(link.contents[0].strip().encode('utf-8'))
        return


    def list_heading_NYT_2(self,base_url):
        html = urllib.urlopen(base_url).read()
        soup = BeautifulSoup(html, 'html.parser')
        print " The title is : ", soup.title , "\n", "  The title name is :" , soup.title.name, '\n'
        tags = soup("h2",{'class':"story-heading"})
        for tag in tags:
            if tag.a:
                print tag.a.text.strip().replace('\n','').encode('utf-8')
            else:
                print tag.contents[0].strip().encode('utf-8')
        return

    def print_more(self):
        if (raw_input("contninu (y/n") == 'n'):
            return 'break'
        else:
            return 'continue'

    def website_article_as_text(self):
        base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
        html = requests.get(base_url)
        soup = BeautifulSoup(html.text, 'html.parser')
        story1 = soup.find_all('div',{"class:","content drop-cap"})
        count =0
        for line in story1:
            print line.text.encode('utf-8')
            print self.print_more()
        story = soup.find_all('section',{"class:","content-section"})
        for line in story:
            print line.text.encode('utf-8')
            self.print_more()
        return

    def print_url(self):
        html = self.open_base_url_Vanity()
        soup= BeautifulSoup(html,'html.parser')
        tags = soup.find_all('a')
        count =0
        for link in tags:
                print link.get('href')
                count+=1
        print " Total links are" , count
        return

    def open_base_url_Vanity(self):
        base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
        html = urllib.urlopen(base_url).read()
        return html

    def print_url_re(self):
        html = self.open_base_url_Vanity()
        links = re.findall( 'href="http://.*?"' ,html)
        print " the Total length is ," , len(links)
        for link in links:
            print link
        return


    def travel_xml(self):
        '''
            <bookstore>
            <book category="cooking">
            <title lang="en">Everyday Italian</title>
            <author>Giada De Laurentiis</author>
            <year>2005</year>
            <price>30.00</price>
        </book>  '''
        ''' if reading from a string then use tree=ET.fromstring(string-name)'''
        tree = ET.parse(file_xml)
        root = tree.getroot()
        print " root name: {} and attrib is{} ".format(root.tag , root.attrib)
        print " The name of first element {}, it items are {} and keys are {}".format(root[0].tag, root[0].items(), root[0].keys())
        # find the refrence of all records
        books = root.findall('book')
        ls =[]
        for item in list(root[0]):
            ls.append(item.tag)
        for bk in books:
                print "\n"
                print bk.tag, bk.attrib
                for item_name in ls:
                    print bk.find(item_name).text
        return

    def travel_xml_for_any_file(self):
        '''Print the name of Elemets and sub Elements
                we have one child 'book and that has 4 more subelement This program will print Child and subelement.
                This way we do not have to remember the number of elements
                Remaining work
                1.Automatically find the numbers of the element '''
        tree = ET.parse('C:\\Users\\himan\\Documents\\Himani-Data\\Git-Working\\practice_python\\Config\\books.xml')
        root = tree.getroot()
        print "\n\nAnother way of printing "
        print " root name {} and attrib is {} and root[0].tag {}".format( root.tag, root.attrib , root[0].tag)
        #root.findall(root[0].tag) ==> will give the  pointer to each location
        total_record = len(root.findall(root[0].tag))
        total_item = len(list(root[0]))
        print " Printing the number of items"
        for item in list(root[0]):
            print item.tag

        for i in range(0, total_record):
            print '\n'
            print root[i].tag , root[i].attrib
            for j in range(0, total_item):
                print '{:10}{:20}'.format(root[i][j].tag, root[i][j].text)
        return
    def print_dict(self,obj_dict):
        for k in obj_dict:
            print k, obj_dict[k]
        return

    def is_dict(self,dataObj):
        for item in dataObj:
            print "\nrecond :-"
            for  inter_list in item:
                if isinstance(item[inter_list],dict):
                    self.print_dict(item[inter_list])
                elif type(item[inter_list])==list:
                    for value in item[inter_list]:
                        if isinstance(value,dict):
                            self.print_dict(value)
                        else:
                            print value
                else:
                    print  item[inter_list]

    def travel_json(self):
        # will read a json file and print the element
        with open(file_json,'r')as data_file:
            data = json.load(data_file) #load for file and loads for string
         # data is this is dict with one single item in the list
        json_key = (data.keys()[0]).encode('utf=8')
        self.is_dict(data[json_key])
        # print all items in json
        '''for item in data[json_key]:
            print "\nrecond :-"
            for  inter_list in item:
                if isinstance(item[inter_list],dict):
                    print_dict(item[inter_list])
                elif type(item[inter_list])==list:
                    for value in item[inter_list]:
                        if isinstance(value,dict):
                            print_dict(value)
                        else:
                            print value
                else:
                    print  item[inter_list]'''
        return



    def http_connect(self):
        conn = httplib.HTTPConnection('www.google.com',80)
        url = '/index.html'
        conn.request("GET", url)
        resp = conn.getresponse()
        print resp.getheaders()
        print resp.getheader('location')


        return