# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:35:18 2020

@author: A
"""

a = 99
if a < 100:
    print("a는 100보다 작습니다.")
    print("좋았어")

a = 200

if a < 100:
    print("100보다 작군요.")
    print("거짓이므로 이 문장은 안보이겠죠?")

print("프로그램 끝")

a = 200

if a < 100 :
    print("100보다 작군요.")
else :
    print("100보다 크군요.")
    

a = int(input("구입금액을 입력하시오! "))
if a > 100000:
    print("""구입금액이 100,000원을 초과하여 %d원 할인된 지불 금액은 %d원 입니다.""" %(a*0.05,a*0.95))
else :
    print("구입금액은 %d원입니다." %a)
    
x = 3
y = 2
x > y

x < y

x == y

x != y

x >= y

x <= y

money = 2000
if money > 3000 :
    print("택시를 타쟛!")
else :
    print("에효, 걸어가야겠다.")
   
luggage = float(input("짐의 무게가 얼마입니까? "))
if luggage > 20 :
    print("무거운 짐은 20,000원을 내셔야합니다.")
else :
    print("짐에대한 수수료는 없습니다.")
print("감사합니다.")

tempeture = float(input("현재 기온은 몇 도씨입니까? "))
if tempeture > 30 :
    print("반바지를 입으세요")
else :
    print("긴바지를 입으세요")
print("나가서 운동하세요")

num = int(input("정수를 입력하세요! "))
if num % 2  == 0 :
    print("짝수를 입력했군요.")
else :
    print("홀수를 입력했군요.")

money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else :
    print("걸어가라")
    
1 in [1, 2, 3]
1 not in [1, 2, 3]

'a' in ('a', 'b', 'c')
'j' not in 'python'

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print("택시를 타고 가라")
else :
    print("걸어가라")
    
pocket = ['paper', 'cellphone', 'money']
if "card" in pocket :
    print("버스를 타고가라")
else :
    print("걸어가라")
    
pocket = ['paper', 'cellphone', 'money']    
if 'money' in pocket :
    pass
else :
    print("카드를 꺼내라")
    
a = 75

if a > 50 :
    if a < 100 :
        print("50보다 크고 100보다 작군요")
    else :
        print("와~ 100보다 크군요.")
else :
    print("에고~ 50보다 작군요.")

a = int(input("점수를 입력하세요! "))

if a >= 60 :
    if a>= 70 :
        if a >= 80 :
            if a >= 90 :
                print("A")
            else : print("B")
        else : print("C")
    else : print("D")
else : print("F")

score = int(input("점수를 입력하세요 : "))

if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")
    
score = int(input("점수를 입력해주세요 : "))
if score >= 95 :
    print("A+")
elif score >= 90 :
    print("A0")
elif score >= 85 :
    print("B+")
elif score >= 80 :
    print("B0")
elif score >= 75 :
    print("C+")
elif score >= 70 :
    print("C0")
elif score >= 65 :
    print("D+")
elif score >= 60 :
    print("D0")
else : print("F")

score = 57

if score >= 60:
    print("합격이다")
elif score >= 40 :
    print("불합격이지만 과락은 아닙니다.")
else : print("불합격이면서 과락입니다.")

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket :
    print("택시를 타고가라")
elif card :
    print("택시를 타고가라")
else :
    print("걸어가라")
    
    
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket or card :
    print("택시를 타고가라")
else :
    print("걸어가라")
    
no1 = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 "))
if no1 == 1 :
    no1_1 = input("수식을 입력하세요: ")
    print(no1_1,"결과는 %f 입니다." %(eval(no1_1)))
elif no1 == 2 :
    no2_1 = int(input("첫 번째 숫자를 입력하세요 "))
    no2_2 = int(input("두 번째 숫자를 입력하세요 "))
    print("합계는 %d 입니다." %(no2_1+no2_2))
else :
    print("1 또는 2를 선택해주세요!")
    
month = int(input("월을 입력하세요 "))
if month == 2 :
    print("%d월의 날 수는 29일 입니다" %month)
elif month in (4, 6, 9, 11) :
    print("%d월의 날 수는 30일 입니다" %month)
else :
    print("%d월의 날 수는 31일 입니다" %month)
    
i = 0
while i < 3:
    print("%d : 안녕하세요? while문을 공부중입니다. ^^" %i)
    i = i + 1
    
i, hap = 0, 0

i = 1
while i < 11 :
    hap = hap + i
    i = i + 1

print("1에서 10까지의 합계 : %d" %hap)


a="1"
b="2"
c="*"
d=a+c+b
eval(d)


hap=0
a,b=0,0
while True:
    a= int(input("계산할 첫번째 수를 입력하세요 :"))
    b= int(input("계산할 두번째 수를 입력하세요 :"))
    c= input("계산할 연산자를 입력하세요 :")
    if(c=="+"):
        print("%d + %d = %d" %(a,b,a+b))
    elif(c=="-"):
        print("%d - %d = %d" %(a,b,a-b))
    elif(c=="*"):
        print("%d * %d = %d" %(a,b,a*b))
    elif(c=="/"):
        print("%d / %d = %d" %(a,b,a/b))
    elif(c=="%"):
        print("%d % %d = %d" %(a,b,a%b))
    elif(c=="//"):
        print("%d // %d = %d" %(a,b,a//b))
    elif(c=="**"):
        print("%d ** %d = %d" %(a,b,a**b))
    else:
        print("연산자를 다시 입력해 주세요")
    
    
    
while True:
    a= input("계산할 첫번째 수를 입력하세요 :")
    b= input("계산할 두번째 수를 입력하세요 :")
    c= input("계산할 연산자를 입력하세요 :")
    d=a+c+b
    a=int(a)
    b=int(b)
    d=eval(d)
    print("%d %s %d = %d" %(a,c,b,d))



hap=0
a,b=0,0
while True:
    a=int(input("더할 첫 번째 수를 입력하세요 : "))
    if a==0:
        break
    b=int(input("더할 두 번째 수를 입력하세요 : "))
    hap=a+b
    print("%d+%d=%d" %(a,b,hap))
print("0을 입력해 반복문을 탈출했습니다.")


treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        

coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee=coffee-1
    print("남은 커피의 양은 %d 개 입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break




coffee=10
while True:
    money=int(input("돈을 넣어 주세요: "))
    if money==300:
        print("커피를 줍니다.")
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d 를 주고 커피를 줍니다."%(money-300))
        coffee=coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d 개 입니다." %coffee)
    if coffee==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
        





























