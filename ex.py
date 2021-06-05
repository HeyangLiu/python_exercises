from datetime import date
from datetime import datetime
import math
import calendar
import os.path
import os
import platform
import multiprocessing
def main():
    """
    #date n time
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    #ask r give area of circle and volume of sphere
    r = float(input("r = "))
    print(math.pi*r*r)
    print(math.pi*r*r*r*4/3)
    
    #enter nums seprated by comma, return list n tuple
    nums = input("enter: ")
    l = nums.split(",")
    t = tuple(l)
    print("list: ", l)
    print("tuple: ", t)
    # output 1st n last elem
    print(l[0], l[-1]) 
    #accecpt int n return n+nn+nnn
    n = int(input("enter n: "))
    print(3*n+20*n+100*n)
    #print document
    print(abs.__doc__)
    #print given month year
    c = calendar.TextCalendar(calendar.SUNDAY)
    year = int(input("enter year: "))
    mon = int(input("enter month: "))
    print(c.formatmonth(year, mon))
    #date diff
    date1 = date(2019, 10, 8)
    date2 = date(2019, 10, 16)
    print(date2-date1)
    print((date2-date1).days)
    #get the difference between a given number and 17, 
    #if the number is greater than 17 return double the absolute difference
    x = int(input("enter x: "))
    print(abs(x-17))
    if x-17 > 0:
        print(2*(x-17))
    s = "mIs this"
    #add "Is" if not start with "Is"
    if(s[0]=='I' and s[1]=='s'):
        print(s);
    else:
        s="Is"+s
        print(s)
    #n copies of str
    s = "this"
    n = 5
    res = ""
    for i in range (n):
        res+=s
    print(res)
    #even or odd
    x = int(input("enter x: "))
    if(x%2==0):
        print("even")
    else:
        print("odd")
    #n copies of 1st 2 chars of str
    s = "ws"
    n = 4
    l = 2
    if len(s)<l:
        l=len(s)
    substr = s[:l]

    res = ""
    for i in range (n):
        res += substr
    print(res)
    # test letter vowel
    s = "desktop"
    v = "aeiou"
    for i in range (len(s)):
        if s[i] in v:
            print(s[i], "is a vowel")
        else:
            print(s[i], "is not a vowel")
    # greatest common divisor
    x = 36
    y = 24
    if(x%y==0):
        print(y)
    else:
        for i in range(int(y/2), 0, -1):
            if(x%i==0 and y%i==0):
                print(i)
                break
    
    #least common multiple
    x = 36
    y = 24
    gcd = 0
    if(x%y==0):
        print(y)
    else:
        for i in range(int(y/2), 0, -1):
            if(x%i==0 and y%i==0):
                gcd = i
                break
    print(int(x*y/gcd) ) 
    #if both are int, return sum
    x= 23
    y=89
    if(isinstance(x, int) and isinstance(y, int)):
        print(x+y)
    else:
        print("error")
    #check if a file exist
    f = "calendars_start.py"
    open(f, 'w')
    print(os.path.isfile(f))
    #check os name, platform n release info
    print(os.name)
    print(platform.system())
    print(platform.release())
    # check # of cpu using
    print(multiprocessing.cpu_count())
    #get ascii value of char
    print(ord('a'))
    #empty a var without destroy it
    x = 15
    print(type(x)())
    #int to binary and hex
    x=28
    print(format(x, "08b"))
    print(format(x, "08x"))"""
    # for loop
    for i in range (0, 10, 2):
        print(i)

    
   


if __name__ == "__main__":
    main()