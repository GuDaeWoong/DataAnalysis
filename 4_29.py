# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:31:01 2020

@author: A
"""

a=input("교환할돈을 얼마:")

print(")


a=5
b=3
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)


a,b,c=2,3,4
print(a+b-c,a+b*c,a*b/c)


s1,s2,s3="100","100.123","99999999999"
print(int(s1)+1,float(s2),int(s3)+1)

a=100
b=100.123
str(a)+'1'
str(b)+'1'


a=10

a+=5;print(a)
a-=5;print(a)
a*=5;print(a)
a/=5;print(a)
a//=5;print(a)
a%=5;print(a)
a**=5;print(a)


##변수선언##

money,c500=0,0
money=int(input("얼마나 교환하시겠습니까? : "))
c500=money//500
money%=500
c100=money//100
money%=100
c50=money//50
money%=50
c10=money//10
money%=10
print("\n 500원짜리 ==> %d개" %c500) 
print("\n 100원짜리 ==> %d개" %c100) 
print("\n 50원짜리 ==> %d개" %c50) 
print("\n 10원짜리 ==> %d개" %c10) 
print("\n 바꾸지 못한 잔돈은 ==> %d원" %money) 




money,c50000=0,0
money=int(input("얼마나 교환하시겠습니까? : "))
c50000=money//50000
money%=50000
c10000=money//10000
money%=10000
c5000=money//5000
money%=5000
c1000=money//1000
money%=1000
print("\n 50000원짜리 ==> %d개" %c50000) 
print("\n 10000원짜리 ==> %d개" %c10000) 
print("\n 5000원짜리 ==> %d개" %c5000) 
print("\n 1000원짜리 ==> %d개" %c1000) 
print("\n 바꾸지 못한 잔돈은 ==> %d원" %money) 



a,b=100,200
print(a==b,a!=b,a>b,a<b,a>=b,a<=b)



a="Life is too short, You need Python"
a[0]
a[-2]
a[-5]
b=[0]+a[1]+a[2]+a[3]
b

a[0:4]
a[19:]
a[:17]
a[:]
a[19:-7]




a="20010331Rainy"
date=a[:8]
seather=a[8:]
year=a[:4]
day=a[4:8]


a="piton"
a[1]
a[1]='y'


a = "Pithon"
a[:1]
a[2:]
a[:1] + 'y' + a[2:]

pin="881120-1068234"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)


string="orajava"

print(string)
string[3:]
string[:3]
string[:4]




number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)


"%10s" %"hi"
"%-10sjane." %"hi"

"%10.4f" %3.42134234




a="hobby"
a.count("b")
a.find("b")

a = "Python is best choice"
a.find("b")
a.find("k")


a = "Life is too short"
a.index("t")
a.index("k")

a=","
a.join("abcd")

a="hi"
a.upper()
a = " hi "
a.lstrip()
a.rstrip()
a.strip()

a = "Life is too short"
a.replace("Life", "Your leg")

a = "Life is too short"
a.split()
b = "a:b:c:d"
b.split(':')

odd = [1, 3, 5, 7, 9]


a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]




a = [1, 2, 3]

a[0]
a[-1]

a = [1, 2, 3,4,5]
a[0:2]



a=[1,2,3]
b=[4,5,6]
a+b

a*3


a=[1,2,3]
a[2]=4
a
a[1:2]=["a","b","c"]

a=[1, 'a', 'b', 'c', 4]
a[1:3]=[]
a
del a[1]
a

a=[1,2,3]
a.append(4)
a

#정렬
a=[1,4,3,2]
a.sort()
a

#순서 뒤집기
a=["a","c","b"]
a.reverse()

#위치반환
a=[1,2,3]
a.index(3)


#리스트 요소 끄집어내기
#마지막 요소를 돌려주고 그 요소는 삭제하는 함수
a=[1,2,3]
a.pop()
a

#리스트에 포함된 요서 x의 개수 세기
a=[1,2,3,1]
a.count(1)

a=[1,2,3]
a.extend([4,5])
a
b=[6,7]
a.extend(b)

a,b,c,d,=0,0,0,0
hap=0
a=int(input("1번째 숫자 : "))
b=int(input("2번째 숫자 : "))
c=int(input("3번째 숫자 : "))
d=int(input("4번째 숫자 : "))
hap=a+b+c+d

print("합계 == > %d" %hap)





aa=[0,0,0,0]
hap=0
aa[0]=int(input("1번째 숫자 : "))
aa[1]=int(input("2번째 숫자 : "))
aa[2]=int(input("3번째 숫자 : "))
aa[3]=int(input("4번째 숫자 : "))
hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계 == > %d" %hap)


aa=[]
aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)
print(aa)

aa=[]
for i in range(0,100):
    aa.append(2)

len(aa)
print(aa)

t1=(1,2,"a","b")

t11=[1,2,"a","b"]

#지우기 변경 불가능 
del t1[0]
t1[0]="c"

t1[0]

t1[3]
t1[1:]

t2=(3,4)

t1+t2

t2*3
#튜플생성
tt1=(10,20,30)
tt2=10,20,30
tt2

tt3=(10)
tt4=10
tt5=(10,)
tt6=10,


tt1.append(40)
tt1[0]=40
del(tt1[0])

del(tt1)


tt1=(10,20,30,40)
tt2=("a","b")
tt1+tt2
tt2*3

myTuple=(10,20,30)
myList=list(myTuple)
myList.append(40)
myTuple=tuple(myList)
myTuple

dic={"name":"pay","phone":"0119993323","birth":"1118"}
dic

a={1:"a"}
a[2]="b"
a


del a[1]
a
a["name"]="pey"
a[3]=[1,2,3]

a={"name":"pey",3:[1,2,3],2:"b"}
grade={"pey":10,"julliet":99}
grade["pey"]
grade["julliet"]
a={1:"a",1:"b"}


a={"name":"pay","phone":"0119993323","birth":"1118"}
a.keys()
a.values()


a.items()

a.clear()

student={"학번":1000,"이름":"홍길동","학과":"컴퓨터학과"}

student["핸드폰"]="123-456-789"

student['이름']

a={"name":"pay","phone":"0119993323","birth":"1118"}
a.get("name")
a.get("phone")

"name" in a

"email" in a




myList=[30,10,20]


myList
myList.append(40)
myList.pop()

myList
myList.sort()
myList
myList.reverse()
myList

myList.insert(2,222)
myList
myList.remove(222)
myList


myList.extend([77,88,77])
myList
myList.count(77)

s1=set([1,2,3])
s2=set("hello")

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
#공집합
s1 & s2
s1.intersection(s2)
#합집합
s1 | s2
s1.union(s2)
#차집합
s1-s2
s2-s1
s1.difference(s2)
s2.difference(s1)

#1개추가
s1=set([1,2,3])
s1.add(4)
#여러개 추가
s1=set([1,2,3])
s1.update([4,5,6])
s1
#특정값 제거
s1=set([1,2,3])
s1.remove(2)

mySet1={1,2,3,3,3,4}
mySet1
salesList=["삼각김밥","바나나","도시락","삼각김밥","삼각김밥","도시락","삼각김밥"]
set(salesList)


mySet1={1,2,3,4,5}
mySet2={4,5,6,7}

mySet1.intersection(mySet2)
mySet1 & mySet2

mySet1.union(mySet2)
mySet1 | mySet2

mySet1.difference(mySet2)
mySet1 - mySet2
#대칭 차집합 서로없는것들만 나옴
mySet1 ^ mySet2
mySet1.symmetric_difference(mySet2)


a=[1,2,3,4]
while a:
    print(a.pop())
    

a=3

#############
#1 colors = ['red', 'blue', 'green'] 가 있을때 결과가 아래와 같이 나오도록 하세요.

colors=["red","blue","green"]
1-1) red
1-2) green
1-3) 3  ==> 리스트 길이를 출력

1-1) colors[0]
1-2) colors[2]
1-1) len(colors)

#2 string = "python1" 일 때 아래와 같은 결과가 나오도록 출력해 보세요.(슬라이싱)
2-1) python1
2-2) hon1
2-3) pyt
2-4) pyth
2-5) python


striong="python1"
2-1) striong
2-2) striong[3:]
2-3) striong[:3]
2-4) striong[:4]
2-5) striong[:]

#3color1과 color2가 아래와 같을 때 3-1) ~ 3-3)의 결과가 나오도록
color1=["red","blue","green"]
color2=["orange","blacke","white"]

3-1) ['red', 'blue', 'green', 'orange', 'blacke', 'white']
3-2) ['red', 'blue', 'green', 'red', 'blue', 'green']
3-3) ['red', 'blue', 'green', 'orange', 'black']

3-1) color1 + color2
3-2) color1 + color1
3-3) color1 + color2[:2]


#4  2차원 리스트의 예이다. 각 문제의 출력되는 결과를 예측하시오.
myList = [ [ 1,  2,  3,  4] ,
         [5,  6,  7,  8] ,
         [9, 10,  11, 12] ]

4-1) myList [0][1]
4-2) myList [1][3]
4-3) myList [2]

4-1)  2
4-2)  8
4-3)  [9,10,11,12]

#5 다음과 같은 리스트가 있을 때, 출력 결과가 아래와 같게 해 보세요
test = [ '설현' , '초아' , '지민', '유나' , '유경', '혜정' , '민아', '찬미' ]

5-1) '지민' 
5-2) '민아'  
5-3) ['설현'] 
5-4) ['민아', '찬미']  
5-6) ['초아', '지민'] 
5-7) ['초아', '유경', '찬미']

5-1) test[2]
5-2) test[-2] ; test[6]
5-3) test[:1]
5-4) test[6:8]
5-6) test[1:3]
5-7) test[1:2]+test[4:5]+test[7:8]



#q1
길동={"국어":80,"영어":75,"수학":55}

(길동['국어']+길동['영어']+길동['수학'])/3

#q2
13%2==1
True 일경우 홀수
#q3
길동={"주민등록번호":"881120-1068234"}
길동["주민등록번호"][:6]
길동["주민등록번호"][7:]
#q4
pin = "881120-1068234"
pin[7]
#q5
a = "a:b:c:d"
a.replace(":","#")
#q6
a=[1,3,5,4,2]
a.sort()
a.reverse()
a
#q7
a=['Life', 'is', 'too', 'short']
" ".join(a)
#q8
a=(1,2,3)
type(a)
a=a+(4,)
#q9
a = dict()

1.a['name'] = 'python'
2.a[('a',)] = 'python'
3.a[[1]] = 'python'
4.a[250] = 'python'

3번 

#q10
a = {'A':90, 'B':80, 'C':70}
a.pop("B")

#q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set(a)
#q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
b는 [1, 4, 3] 값이 올것이다 
a와 b는 동일하다고 하였기때문에 a를 변경할시 b도 같이 변경된다
