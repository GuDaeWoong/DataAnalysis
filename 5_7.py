# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:36:13 2020

@author: A
"""

a=0
while a<3:
    print("안녕하세요 for문을 공부중 입니다")
    a+=1
 
    
    
    
for i in range(0,3,1):
    print("안녕하세요 for문을 공부중 입니다")

for i in range(3):
    print("안녕하세요 for문을 공부중 입니다")
    
    
#range(시작값,끝값+1,증가값)
#range(3) 0에서 3개


for i in range(3):
    print("%d : 안녕하세요 for문을 공부중 입니다" %i)
    
for i in range(1,6,1):
    print("%d " %i, end=" ")
    
a=["철수","영희","길동","유신"]
for i in range(4):
    print("안녕!",a[i])
    
for i in range(5):
    print("환영합니다")


for i in range(1,10,2):
    print(i)

for i in ["americano","latte","frappuccino"]:
    print(i)
    

for i in "abcdefg":
    print(i)

for i in range(10,1,-1):
    print(i)

for i in range(20,3,-4):
    print(i)


a=1
while a<10:
    print("9 X %d = %d" %(a,a*9))
    a+=1



a=int(input("구구단 몇 단을 계산할까요!(1~9)? : \n"))
b=1
print("구구단 %d 단을 계산합니다"%a)
while b<10:
    print("%d X %d = %d" %(a,b,a*b))
    b+=1


hap=0
i=0
for i in range(1,11,1):
    hap=hap+i
print("1에서 10까지의 합계 : %d" %hap)


#500과 1000사이에 홀수의 합
hap=0
i=0
for i in range(51,101,2):
    hap=hap+i
print("1에서 10까지의 합계 : %d" %hap)

hap=0
i=0
for i in range(0,100,7):
    hap=hap+i
print("1에서 10까지의 합계 : %d" %hap)

hap=0
i=0
num=0

num=int(input("값을 입력하세요 : "))
for i in range(1,num+1,1):
    hap+=i
print("1에서 %d까지의 합계 : %d" %(num,hap))



st=int(input("시작값을 입력하세요 : "))
ls=int(input("끝값을 입력하세요 : "))
t=int(input("증가값을 입력하세요 : "))
hap=0
i=0
for i in range(st,ls+1,t):
    hap+=i
print("1에서 %d까지의 합계 : %d" %(num,hap))




a=int(input("구구단 몇 단을 계산할까요!(1~9)? : "))
print("구구단 %d 단을 계산합니다"%a)
for i in range(9,0,-1):
    print("%d X %d = %d" %(a,i,a*i))
    


for i in range(0,3,1):
    for k in range(0,2,1):
        print("파이썬은 꿀잼입니다. (i값: %d,k값: %d)"%(i,k))

i,k=0,0

for i in range(2,10,1):
    print("##%d단##"%i)
    for j in range(1,10,1):
        print("%d X %d = %d" %(i,j,i*j))
    print("")
    
for i in range(1,100):
    print("for문을 %d번 실행했습니다." %i)
    break


hap,i=0,0
for i in range(1,101):
    hap+=i
    if hap >=1000:
        break
print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d" %i)


hap,i=0,0
for i in range(1,101,2):
    hap+=i
    if hap >=1000:
        break
print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d" %i)

hap,i=0,0
for i in range(1,101):
    if i%3==0:
        continue
    hap+=i
print("1~100의 합계(3의 배수 제외) : %d"%hap)

aa=[]
aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)
print(aa)

aa=[]
for i in range(0,100):
    aa.append(0)
len(aa)

aa=[0,0,0,0]
hap=0
aa[0]= int(input("1번째 숫자 :"))
aa[1]= int(input("2번째 숫자 :"))
aa[2]= int(input("3번째 숫자 :"))
aa[3]= int(input("4번째 숫자 :"))

hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계==> %d"%hap)

aa=[]
for i in range(0,4):
    aa.append(0)
hap=0

for i in range(0,4):
    aa[i]=int(input(str(i+1)+"번째숫자 :"))
hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계==> %d"%hap)

test_list=["one","two","three"]
for i in test_list:
    print(i)


a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first,last)
    
    
a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
    
    
marks=[90,25,67,45,80]
number=0
for i in marks:
    number+=1
    if i >=60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)
        


marks=[90,25,67,45,80]
number=0
for i in marks:
    number+=1
    if i <60:
        continue
    print("%d번 학생은 합격입니다."%number)
    





for i in range(2,10):
    for j in range(1,10,):
        print(i*j,end=" ")
    print("")


for i in range(2,10):
    for j in range(1,10,):
        print("%d X %d = %d" %(i,j,i*j),end=" ")
    print("")



numList=[]
for i in range(1,6):
    numList.append(i)
numList

numList=[num*num for num in range(1,6)]
numList

numList=[num for num in range(1,21) if num%3==0]


a=[1,2,3,4]
result=[num*3 for num in a]

result=[num*3 for num in a if num%2 ==0]

result=[x*y for x in range(2,10)
for y in range(1,10)]
print(result)



coffee=0
coffee=int(input("어떤 커피 드릴까요?(1.보통,2.설탕,3.블랙) "))
print()
print("#1. 뜨거운 물을 준비한다.")
print("#2. 종이컵을 준비한다.")
      
if coffee==1:
    print("#3. 보통커피를 탄다.")
elif coffee==2:
    print("#3. 설탕커피를 탄다.")
elif coffee==3:
    print("#3. 블랙커피를 탄다.")
else:
    print("#3. 아무거나 탄다.\n")
    
print("#4. 물을 붓는다.")
print("#5. 스푼으로 젓는다.")
print()
print("손님~ 커피 여기 있습니다.")



coffee=0
def coffee_machine(button):
    print()
    print("#1. 뜨거운 물을 준비한다.")
    print("#2. 종이컵을 준비한다.")
      
    if coffee==1:
        print("#3. 보통커피를 탄다.")
    elif coffee==2:
        print("#3. 설탕커피를 탄다.")
    elif coffee==3:
        print("#3. 블랙커피를 탄다.")
    else:
        print("#3. 아무거나 탄다.\n")
              
    print("#4. 물을 붓는다.")
    print("#5. 스푼으로 젓는다.")
    print()
   
coffee=int(input("A손님 어떤 커피 드릴까요?(1.보통,2.설탕,3.블랙) "))
coffee_machine(coffee)
print("A손님 ~ 커피 여기 있습니다.")
    
coffee=int(input("B손님 어떤 커피 드릴까요?(1.보통,2.설탕,3.블랙) "))
coffee_machine(coffee)
print("B손님 ~ 커피 여기 있습니다.")

coffee=int(input("C손님 어떤 커피 드릴까요?(1.보통,2.설탕,3.블랙) "))
coffee_machine(coffee)
print("C손님 ~ 커피 여기 있습니다.")

#1.
print("1. for 문을 사용하여 구구단을 아래와 같이 출력해보세요")
for i in range(1,10):
    for j in range(2,10,):
        print("%d X %d = %d" %(j,i,i*j),end=" ")
    print("")
    
#2.
for i in range(9,1,-1):
    print("#%d단#"%i,end=" ")
print("")
for i in range(9,0,-1):
    for j in range(9,1,-1):

        print("%d X %d = %d" %(j,i,i*j),end=" ")
    print("")


#3.
a="i like you"
b=reversed(a)
for i in b:
    print(i,end="")
    

a="i like you"
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")

#4.
a=int(input("입력하시오 : "))
for i in range(1,a):
    a*=i

print("%d!은 %d입니다."%(i+1,a))