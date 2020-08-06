# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:37:00 2020

@author: A
"""


def plus(v1,v2):
    result=0
    result=v1+v2
    return result

hap=0
hap=plus(100,200)
print("100과 200의 plus() 함수의 결과는 %d" %hap)

def calc(v1,v2,op):
    result=0
    if op=="+":
        result=v1+v2
    elif op=="-":
        result=v1-v2
    elif op=="*":
        result=v1*v2
    elif op=="/":
        result=v1/v2
    elif op=="**":
        result=v1**v2
    return result
    

res=0
var1,var2,oper=0,0,"" 

var1=int(input("1번째 숫자를 입력하세요 : "))
oper=input("연산자를 입력하세요(+,-,*,/,**) : ")
var2=int(input("2번째 숫자를 입력하세요 : "))

if var2==0 and oper=="/":
    print("0으로 나누면 안되요")
else:
    res=calc(var1,var2,oper)
    print("계산기 : %d %s %d = %d" %(var1,oper,var2,res))
    
def func1():
    a=10
    print("func1()에서 a값 %d"%a)

def func2():
    print("func2()에서 a값 %d"%a)
#a=20
func1()
func2()


def func1():
    global a #이함수안에서 a는 전역 변수
    a=10
    print("func1()에서 a값 %d"%a)
    
def func2():
    print("func2()에서 a값 %d"%a)
a=20
func1()
func2()



def func1():
    result=100
    return result
def func2():
    print("반환값이 없는 함수 실행")
    
hap=0
hap=func1()
print("func1()에서 돌려준 값==>%d"%hap)
func2()


def multi(v1,v2):
    retList=[]
    res1=v1+v2
    res2=v1-v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList=[]
hap,sub=0,0

myList=multi(100,200)
hap=myList[0]
sub=myList[1]
print("multi()에서 돌려준 값==>%d %d "%(hap,sub))



def myFunc():
    pass

if True:
    pass
else:
    print("거짓이네요")

def para2_func(v1,v2):
    result=0
    result=v1+v2
    return result

def para3_func(v1,v2,v3):
    result=0
    result=v1+v2+v3
    return result


hap=0
hap=para2_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==>%d" %hap)
hap=para3_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==>%d" %hap)


def para_func(v1,v2,v3=0):
    result=0
    result=v1+v2+v3
    return result
hap=0
hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==>%d" %hap)
hap=para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==>%d" %hap)


def para_func(*para):
    result=0
    for num in para:
        result=result+num
    return result
hap=0
hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==>%d" %hap)
hap=para_func(10,20,30,40,50)
print("매개변수가 5개인 함수를 호출한 결과 ==>%d" %hap)



def dic_func(**para):
    for k in para.keys():
        print("%s-->%d명입니다." %(k,para[k]))

dic_func(트와이스=9,소녀시대=7,걸스데이=4,블랙핑크=4)


def mult(a,b):
    c=0
    c=a*b
    return c

a=mult(200,88)
print(a)

def mult_1(a,b):
    if a>b:
        return a
    else:
        return b
    

mult_1(0,1)


import random
def getNumber():
    return random.randrange(1,46)
lotto=[]
num=0

print("**로또 추첨을 시작합니다 . **\n")
while True:
    num=getNumber()
    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto)>=6:
        break

print("추첨된 로또 번호 ==> ",end="")
lotto.sort()
for i in range(0,6):
    print("%d  "%lotto[i],end="")
    
    


import sys
print(sys.builtin_module_names)


import math
dir(math)




def hap(num1,num2):
    res=num1+num2
    return res
print(hap(10,20))
#           매개변수   : 수식
hap2=lambda num1,num2:num1+num2
print(hap2(10,20))

hap3=lambda num1=10,num2=20:num1+num2
print(hap3())
print(hap3(100,200))


myList=[1,2,3,4,5]
def add10(num):
    return num+10

for i in range(len(myList)):
    myList[i]=add10(myList[i])
print(myList)



def selfCall():
    print("하",end="")
    selfCall()
selfCall()



def count(num):
    if num>=1:
        print(num,end="")
        count(num-1)
    else:
        return
count(10)
count(20)



def factorial(num):
    if num<=1:
        return num
    else:
        return num*factorial(num-1)
print(factorial(4))
print(factorial(10))



def say():
    return "Hi"
say()



def sum_many(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
sum_many(1,2,3,4)



def sum_and_mul(a,b):
    return a+b,a*b

result=sum_and_mul(3,4)
result



def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다"%name)
    print("나이는 %d살 입니다"%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
    
    
    
say_myself("구대웅",28)
say_myself("구대웅",28,True)



a=1
def vartest(a):
    a=a+1
    return a
vartest(a)
print(a)



f=open("C:/Python/새파일.txt","w")#r읽기모드 ,w쓰기모드 ,a 추가모드
f.close()


f=open("C:/Python/새파일.txt","w")
for  i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

f=open("C:/Python/새파일.txt","r")
line=f.readline()
print(line)
f.close()



f=open("C:/Python/새파일.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()



f=open("C:/Python/새파일.txt","r")
lines=f.readlines()
for line in lines:
    print(line)
f.close()



f=open("C:/Python/새파일.txt","a")
for i in range(11,20):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()




f=open("foo.txt","w")
f.write("Life is too short, you need python")
f.close()

with open("foo.txt","w") as f:
    f.write("Life is too short, you need python")
    
#with문을 사용하면 with블록을 벗어나는순간 열람 파일 객체f가 자동으로 close된다





f=open("dream1.txt","r")
lines=f.readlines()
for line in lines:
    print(line)
f.close()



with open("dream1.txt","r") as my_file:
    contents=my_file.read()
    word_list=contents.split(" ")
    line_list=contents.split("\n")

print("총 글자의수 : ",len(contents))
print("총 단어의 수 : ",len(word_list))
print("총 줄의 수  : ",len(line_list))


with open("dream1.txt","r") as my_file:
    contents=my_file.readlines()


contents.join("\n")

contents_1="".join(contents)
len(contents_1)






