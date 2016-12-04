import sys
sys.path.append('C:\\Users\\himan\\Documents\\Himani-Data\\Git-Working\\practice_python')
from functions.Web_related_functions import *


if __name__== "__main__":
    choice = ''
    webFun_Ins = WebFun()
    while choice != 'q':
        print '{:5}{:<40}'.format("","Please select the test to run")
        print '{:5}{:<40}'.format("", "q. Please select q to quit")
        print '{:5}{:<40}'.format("","1. Use the BeautifulSoup and request Python packages to print out"
                                     " a list of all the article titles on the New York Times homepage.")
        print '{:5}{:<40}'.format("","2. Print the heading from New York Times page using Beautiful soup and urllib")
        print '{:5}{:<40}'.format("","3. website article on the screen")
        print '{:5}{:<40}'.format("","4. Print URL from the page")
        print '{:5}{:<40}'.format("","5. print URL with reguler express")
        print '{:5}{:<40}'.format("","6. read an xml file ")
        print '{:5}{:<40}'.format("", "7. read an xml file with tags ")
        print '{:5}{:<40}'.format('','8. Json example')
        choice = raw_input("please enter choice ")
        if choice.lower() == 'q':
            break
        elif (choice == '1'):
            webFun_Ins.list_articles_on_NYT("http://www.nytimes.com/")
            break
        elif (choice=='2'):
            webFun_Ins.list_heading_NYT_2("http://www.nytimes.com/")
            break
        elif (choice=='3'):
            webFun_Ins.website_article_as_text()
            break
        elif (choice=='4'):
            webFun_Ins.print_url()
            break
        elif (choice=='5'):
            webFun_Ins.print_url_re()
            break
        elif (choice=='6'):
            webFun_Ins.travel_xml()
            break
        elif (choice=='7'):
            webFun_Ins.travel_xml_for_any_file()
            break
        elif (choice == '8'):
            webFun_Ins.travel_json()
            break
        else:
            print "wrong choice"
