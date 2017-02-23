import sys

filepath='C:\\Users\\himan\\Documents\\Himani-Data\\Git-Working\\practice_python\\Config\\'
def ask():

    while True:
        try:
            x,y = map(int,raw_input("Enter two number to divide ").split())
        except ValueError:
            print "Incorrect value"
        else:
            try:
                 z = x / y
                 print z
            except ZeroDivisionError:
                print "Divided by zero"
            finally:
                print "all Done"

    return

def file_fun():
    Nfile = filepath + sys.argv[1]
    f=open(Nfile,'r')
    print " File line by readlines"
    for w in f.readlines():
        print w.strip()
    print f.tell()
    print f.seek(0)
    for w in f.read():
        print w.strip()


    f.close()
    return

def try_expect():

    try:
        Nfile=filepath+sys.argv[1]
        print Nfile, sys.argv[1]
        f = open(Nfile,'r')
    except IOError:
        print "can't open file"
    else:

            try:
                 s=f.readline()
                 s=int(s.strip())
            except EOFError:
                print " end of file"
                f.close()
                return
            except ValueError:
                print "not a number"
            except:
                print "just pass for other issue"
                raise
            else:
                print "s squre is ", s**2
            finally:
                f.close()
    return


def ps():
    print "This will print phfeonochi serise"
    def fib(n):
        a,b=1,1
        out=[]
        for i in range(n):
            out.append(a)
            a,b=b,a+b

        return out
    print fib(10)
    return

"""Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list."""
def word_len():
    s1="I am a string seven"

    slen= map(lambda x:len(x), (w for w in s1.split()))
    print " the length of each word is" , slen

    print " the reduce function to get the lowest number"
    print reduce(lambda x,y:x if x <y else y, [1,2,45,6,10])
    s1=s1.split()
    print " The word start with s using filter function " , filter(lambda x:x[0]=='s',s1)
    w1=['a','b','c']
    w2=['a1','b1','c1']
    connector ='-'
    print  [w11+connector+w22 for (w11, w22) in zip(w1, w2)]
    return




if __name__=="__main__":
    #try_expect()
    #ps()
    #word_len()
    file_fun()