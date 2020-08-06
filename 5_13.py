import pickle
f=open("test.txt","wb")
data={1:"python",2:"you need"}
pickle.dump(data,f)
f.close()


import pickle #객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
f=open("test.txt","rb")
data=pickle.load(f)
print(data)

import os
os.environ
os.chdir("C:\WINDOWS")
os.getcwd()
os.system("dir")
f=os.popen("dir")
print(f.read())

import shutil #파일복사
shutil.copy("src.txt","dst.txt")

import glob
glob.glob("C:/Users/A/Anaconda3/DataScience/source/names/y*")
glob.glob("../data/names/y*")


import tempfile
filename=tempfile.mktemp()
filename

f=tempfile.TemporaryFile()
f.close()

import time
time.time()

time.localtime(time.time())

time.asctime(time.localtime(time.time()))
time.ctime()

time.strftime("%x",time.localtime(time.time()))
time.strftime("%c",time.localtime(time.time()))


for i in range(10):
    print(i)
    time.sleep(1)
    
import calendar
calendar.weekday(2015,12,31)
print(calendar.calendar(2020))
calendar.prcal(20)
calendar.weekday(2020,5,13)

calendar.monthrange(2020,5)
calendar.prcal(2015)

import random
random.random()
random.randint(1,10)
random.randint(1,100)
data=[1,2,3,4,5]
random.shuffle(data)
data


import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")


####
#1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
#2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력

#3

all([1, 2, abs(-3)-3])
False
chr(ord('a')) == 'a'
True
#4
a= [1, -2, 3, -5, 8, -3]
list(filter(lambda x : x>0, a))
#5
int(hex(234),16)
#6
a=[1, 2, 3, 4]
list(map(lambda x:x*3, a))

#7
a=[-8, 2, 7, 5, -3, 5, 0, 1]
max(a)+min(a)
#8
round(17 / 3,4)
#9


#10
import os
os.environ
os.chdir("C:\doit")
os.getcwd()
os.system("dir")
f=os.popen("dir")
print(f.read())
#11
import glob
glob.glob("C:\doit/*.py")
#12
time.strftime("%Y/%m/%d %H:%M:%S")
#13
list=[]
ran=random.randint(1,45)
for i in range(6):
    while ran in list:
        ran=random.randint(1,45)
    list.append(ran)
list.sort()        
print(list)



#######
#9
f=open("sample.txt","r")
lines=f.readlines()
f.close( )
t = 0

for i in lines:
    score = int(i)  
    t += score
avg = t / len(lines)

f = open("result.txt", "w")
f.write(str(avg))
f.close()

#10
class Calculator:
    def __init__(self,nlist):
        self.nlist = nlist
    def sum(self):
        result=0
        for i in self.nlist:
            result+=i
        return result
    def avg(self):
        result=0
        for i in self.nlist:
            result+=i
        return result/len(self.nlist)
        
cal1 = Calculator([1,2,3,4,5])
cal1.sum() # 합계
cal1.avg() # 평균
cal2 = Calculator([6,7,8,9,10])
cal2.sum() # 합계
cal2.avg()

#11
cd c:\doit
import mymod
print(mymod)
#12
result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)

#첫줄에서 바로 에러나서 인덱스 에러,파이널 로 넘어가기대문에 3+4이다

#13
a="4546793"
a=list(a)
b=[a[0]]
for i in range(len(a)-1) :
    if int(a[i])%2==0 and int(a[i+1])%2==0:
        b.append("*")
        b.append(a[i+1])
    elif int(a[i])%2==1 and int(a[i+1])%2==1:
        b.append("-")
        b.append(a[i+1])
    else:
        b.append(a[i+1])
"".join(b)

#14 ()
a="aaabbcccccca"
b=[a[0]]
count=0
for i in range(len(a)):
    if a[i-1]==a[i]:
        count+=1
    else:
        b+=str(count)+a[i]
        count=1
b+=str(count)
print(b)


        
    
#15
a=["0123456789","01234","01234567890","6789012345","012322456789"]

for i in range(len(a)):
    if a[i].count("0")<=1 and a[i].count("1")<=1 and a[i].count("2")<=1 and a[i].count("3")<=1 and a[i].count("4")<=1 and a[i].count("5")<=1 and a[i].count("6")<=1 and a[i].count("7")<=1 and a[i].count("8")<=1 and a[i].count("9")<=1:
        b="true"
    else:
        b="false"
    print(b,end=" ")
    

