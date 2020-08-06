# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:52:08 2020

@author: A
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b


###
"""
cd c:\doit
import mod1
print(mod1.add(3,4))
"""
###
"""
from mod1 import add,sub
"""


pi=3.141592
class math:
    def solv(self,r):
        return pi*(r**2)

def add (a,b):
    return a+b

if __name__=="__main__":
    print(pi)
    a=math()
    print(a.solv(2))
    print(add(pi,4.4))
    
#################
    #mod2.py
pi=3.141592
class math:
    def solv(self,r):
        return pi*(r**2)

def add (a,b):
    return a+b

if __name__=="__main__":
    print(pi)
    a=math()
    print(a.solv(2))
    print(add(pi,4.4))
    
    
###############
import mod2
print(mod2.pi)
a=mod2.math()
print(a.solv(2))

print(mod2.add(mod2.pi,4.4))

import sys
sys.path
sys.path.append("C:/python/Mymodules")

sys.path.append("C:/doit")

c:\doit>set PYTHONPATH=C:/doit
c:\doit>python

>>> import game.sound.echo
>>> game.sound.echo.echo_test()

>>> from game.sound import echo
>>> echo.echo_test()

>>> from game.sound.echo import echo_test
>>> echo_test()

>>> from game.sound import *
>>> echo.echo_test()


try:
    4/0
except ZeroDivisionError as e:
    print(e)
    
try:
    4/0
except ZeroDivisionError as e:
    print("오류입니다")


print("#프로그램이 시작되었습니다!")
list_a[100]

#1.
pi=3.14
a=int(input("정수입력 : "))
print("원의 반지름 : %d" %a)
print("원의 둘레 : %1.2f" %(a*pi*2))
print("원의 넓이 : %1.2f" %(pi*a**2))
#2.

pi=3.14

a=input("정수입력 : ")
if a.isdigit():#숫자인지 판별
    a=int(a)
    print("원의 반지름 : %d" %a)
    print("원의 둘레 : %1.2f" %(a*pi*2))
    print("원의 넓이 : %1.9f" %(pi*a**2))
else:
    print("정수를 입력해 주세요")


try:
    pi=3.14
    a=int(input("정수입력 : "))
    print("원의 반지름 : %d" %a)
    print("원의 둘레 : %1.2f" %(a*pi*2))
    print("원의 넓이 : %1.2f" %(pi*a**2))
except ValueError as e:
    print("정수를 입력해 주세요")
    
try:
    pi=3.14
    a=int(input("정수입력 : "))
    print("원의 반지름 : %d" %a)
    print("원의 둘레 : %1.2f" %(a*pi*2))
    print("원의 넓이 : %1.2f" %(pi*a**2))
except:
    print("정수를 입력해 주세요")
    
a=[1,2]
try:
    a[3]
except IndexError as e:
    print("다시 입력해 주세요")
    

try:
    f=open("foo.txt",'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data=f.read()
    f.close()

#finally은 try문 수행도중 예외발생 여부에 상관없이 실행
    
f=open("foo.txt",'w')
try:
    #무언가를 수행한다
finally:
    f.close()    #무조건 실행할코드

try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
except IndexError as e:
    print("인덱싱할 수 없습니다.")


try:
    f=open("나없는파일",'r')
except FileNotFoundError:
    pass


class bird:
    def fly(self):
        raise NotImplementedError

class Eagle(bird):
    pass

eagle=Eagle()
eagle.fly()


class Eagle(bird):
    def fly(self):
        print("very fast")
eagle=Eagle()
eagle.fly()

try:
    pi=3.14
    a=int(input("정수입력 : "))
    print("원의 반지름 : %d" %a)
    print("원의 둘레 : %1.2f" %(a*pi*2))
    print("원의 넓이 : %1.2f" %(pi*a**2))

except:
    print("정수를 입력해 주세요")
else:
    print("예외가 발생하지 않음")
    
finally:
    print("프로그램 끝냅니다")



#1
list_number=[12,773,42,172,100]
try:
    a= int(input("정수 입력 :"))
except IndexError as e:
    print("인덱스를 벗어났어요")
except:
    print("정수를 입력해 주세요")
else:
    print("%d번째요소 : %d"%(a,list_number[a]))


#2
lista=["2","소나기","32","장마","125","77"]
a=[]

for i in lista:
    try:
        if i.isdigit():
            a.append(i)
    except:
        pass
    
print(lista,"숫자만 고르면")
print(a,"입니다")   
    

try:
    lista=["2","소나기","32","장마","125","77"]
    a=[]
    for i in lista:
        if i.isdigit():
            a.append(i)
finally:
    print(lista,"숫자만 고르면")
    print(a,"입니다")   
    
    
    
try:
    pi=3.14
    a=int(input("정수입력 : "))
    print("원의 반지름 : %d" %a)
    print("원의 둘레 : %1.2f" %(a*pi*2))
    print("원의 넓이 : %1.2f" %(pi*a**2))

except Exception as e:
    print("type(exception):",type(e))
    print("exception:",e)

        
lista=["2","소나기","32","장마","125","77"]
a=[]

for i in lista:
    try:
        float(i)
        a.append(i)
    except:
        pass
    
print("{}숫자만 고르면".format(lista))
print("{}입니다".format(a))   



abs(3)
abs(-3)
abs(-1.3)
#all은 모두 참이어야 함
all([1,2,3])
all([1,2,3,0]) #0은 거짓
#any하나라도 참이면 트루
any([1,2,3,0])
any([0,""])#0과 빈값은 거짓

chr(97)
chr(48)
chr(65)

dir([1,2,3])

divmod(7,3)
divmod(1.3,0.2)

for i , name in enumerate(["body","foo","bar"]):
    print(i,name)
    
eval("1+2")
eval("'hi'+'a'")
eval('divmod(4,3)')

def positive(x):
    return x>0
print(list(filter(positive,[1,-3,2,0,-5,6])))

print(list(filter(lambda x:x>0,[1,-3,2,0,-5,6])))

hex(234)
hex(3)

a = input()
a


class person:pass
a=person()
isinstance(a,person)

b=3
isinstance(b,person)


sum=lambda a ,b:a+b
sum(3,4)

mylist=[lambda a,b:a+b,lambda a,b:a*b]
mylist
mylist[0](3,4)
mylist[1](3,4)


len("python")
len([1,2,3])
len((1,"a"))


list("python")

def two_times(x):return x*2
list(map(two_times,[1,2,3,4]))
list(map(lambda a:a*2,[1,2,3,4]))

oct(34)
oct(12345)

pow(2,4)
pow(3,3)


#range범위
list(range(5))
list(range(5,10))
list(range(1,10,2))
list(range(0,-10,-1))

sorted([3,1,2])
sorted(["a","b","c"])
sorted("zero")

str(3)
str("hi".upper())

tuple("abc")
tuple([1,2,3])
tuple((1,2,3))



list(zip([1,2,3],[4,5,6]))
list(zip([1,2,3],[4,5,6],[7,8,9]))
list(zip("abc","def"))
list(zip("abc","def",[7,8,9]))


#1
a="a:b:c:d"
"#".join(a.split(":"))
#2
a = {'A':90, 'B':80}
try:
    a = {'A':90, 'B':80}
    a['C']
except KeyError:
    a['C']=70
a['C']  
#3
+의경우 앞이든 뒤에든 붙일수있으나
extend는 무조건 뒤에 붙는다

#4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
b=0
for i in A:
    if i>=50:
        b+=i

sum(list(filter(lambda x : x>50, A)))
#5
a=int(input("n이하까지의 피보나치 수열을 출력 n : "))  
n=[0,1]  
for i in range(2,a):
    n.append(n[i-2]+n[i-1])
print(n)

#6
a=input("숫자를 입력하세요: ")
a=a.split(",")
b=0
for i in a:
    b+=int(i)
print(b)


#7
a=int(input("구구단을 출력할 숫자를 입력하세요(2~9) : "))  
for i in range(1,10):
    print(i*a,end=" " )
#8
with open("abc.txt","r") as f:
    line=f.readlines()
lines.reverse()
with open("abc_reverse.txt","w") as f1:
    for i in range(len(lines)):
        f1.write(lines[i])
