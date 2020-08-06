# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:39:11 2020

@author: A
"""

result=0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))


result1=0
result2=0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))

print(add2(3))
print(add2(7))


class Calculator:          #클래스
    def __init__(self):
        self.result=0

    def add(self,num):      #메서드
        self.result+=num
        return self.result
    
cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))

print(cal2.add(3))
print(cal2.add(7))

-클래스: 객체를 만들기 위한 사용자 정의 자료형
-메서드: 객체의 기능을 반영하여 클래스 내부에 선언된 함수
-객체: 클래스에 의해 정의된 데이터 구조의 인스턴스



def sub(self,num):
    self.result-=num
    return self.result


class cookie:
    pass

a=cookie()
b=cookie()


class FourCal:          #클래스
    def __init__(self):
        self.result=0
    
    def add(self,num):      #메서드
        self.result+=num
        return self.result
    
    def di(self,num):      #메서드
        self.result+=num
        return self.result


class FourCal:
    pass

a=FourCal()
type(a)

a.setdata(4,2)
class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
        
a=FourCal()
a.setdata(4,2)
print(a.first)        
print(a.second)        

a=FourCal()
b=FourCal()
a.setdata(4,2)
print(a.first)

b.setdata(3,7)
print(b.first)



a=FourCla()
b=FourCla()

a.setdata(4,2)
b.setdata(3,7)

id(a.first)

id(b.first)




class FourCla:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result

a=FourCla()
a.setdata(4,2)
print(a.add())



class FourCla:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

a=FourCla()
a.setdata(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())





class FourCla:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result


a=FourCla(4,2)
a.add()

class MoreFourCal(FourCla):
    pass

a=MoreFourCal(4,2)
a.add()

class MoreFourCal(FourCla):
    def pow(self):
        result=self.first**self.second
        return result

a=MoreFourCal(4,2)
a.pow()

a=FourCla(4,0)
a.div()


class SafeFourCla(FourCla):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
        
        
a=SafeFourCla(4,0)
a.div()

class FailFourCla(FourCla):
    def mul(self):
        if self.second==0:
            print("fail")
        else:
            return self.first*self.second
a=FailFourCla(4,0)
a.mul()

class Family:
    lastname="김"
    
print(Family.lastname)

a=Family()

b=Family()

print(a.lastname)
print(b.lastname)

Family.lastname="박"
print(a.lastname)


class car:
    color=""
    speed=0
    
    def upspeed(self,value):
        self.speed+=value
    def downspeed(self,value):
        self.speed-=value


def printmessage():
    print("시험 출력이다.")
    

mycar1=car()
mycar1.color="빨강"
mycar1.speed=0

mycar2=car()
mycar2.color="파랑"
mycar2.speed=0

mycar3=car()
mycar3.color="노랑"
mycar3.speed=0

mycar1.upspeed(30)
print("자동차1의 색상은 %s 이며 현재 속도는 %d km 입니다."
      %(mycar1.color,mycar1.speed))
mycar2.upspeed(60)
print("자동차2의 색상은 %s 이며 현재 속도는 %d km 입니다."
      %(mycar2.color,mycar2.speed))
mycar3.upspeed(0)
print("자동차3의 색상은 %s 이며 현재 속도는 %d km 입니다."
      %(mycar3.color,mycar3.speed))



class car:
    color=""
    speed=0
    
    def upspeed(self,value):
        self.speed+=value
        if self.speed>150:
            self.speed=150

    def downspeed(self,value):
        self.speed-=value
        
mycar1=car()
mycar1.upspeed(1500)
print("자동차1의 색상은 %s 이며 현재 속도는 %d km 입니다."%(mycar1.color,mycar1.speed))





class car:
    color=""
    speed=0
    def __init__(self):
        self.color="빨강"
        self.speed=0
    def upspeed(self,value):
        self.speed+=value
    def downspeed(self,value):
        self.speed-=value

mycar1=car()
mycar2=car()
print("자동차1의 색상은 %s이며 현재 속도는 %dkm입니다"%(mycar1.color,mycar1.speed))
print("자동차2의 색상은 %s이며 현재 속도는 %dkm입니다"%(mycar2.color,mycar2.speed))


class car:
    color=""
    speed=0
    def __init__(self,val1,val2):
        self.color=val1
        self.speed=val2
    def upspeed(self,value):
        self.speed+=value
    def downspeed(self,value):
        self.speed-=value

mycar1=car("빨강",0)
mycar2=car("파랑",20)
print("자동차1의 색상은 %s이며 현재 속도는 %dkm입니다"%(mycar1.color,mycar1.speed))
print("자동차2의 색상은 %s이며 현재 속도는 %dkm입니다"%(mycar2.color,mycar2.speed))


class car:
    name=""
    speed=0
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def getname(self):
        return self.name
    def getspeed(self):
        return self.speed

car1=car("아우디",0)
car2=car("벤츠",30)
print("%s의 현재 속도는 %d 입니다" %(car1.getname(),car1.getspeed()))
print("%s의 현재 속도는 %d 입니다" %(car2.getname(),car2.getspeed()))




class car:
    color=""
    speed=0
    count=0
    def __init__(self):
        self.speed=0
        car.count+=1


mycar1=car()
mycar1.speed=30
#인스턴스 변수
#self를 붙이면 인스턴스 변수
#클래스 변수
#클래스명을 붙이면 클래스 변수
#car.count클래스명 클래스 변수명
#인스턴스명 클래스 변수명 mycar2.count
print("자동차1의 현재 속도는 %dkm,생산된 자동차는 총 %d 입니다" %(mycar1.speed,car.count))



mycar2=car()
mycar2.speed=60
print("자동차1의 현재 속도는 %dkm,생산된 자동차는 총 %d 입니다" %(mycar2.speed,mycar2.count))



class car:
    speed=0
    def upspeed(self,value):
        self.speed+=value
        print("현재 속도(슈퍼 클래스) : %d"%self.speed)
        
class sedan(car):
    def upspeed(self,value):
        self.speed+=value
        if self.speed>150:
            self.speed=150
        print("현재 속도(서브 클래스) : %d"%self.speed)

class truck(car):
    pass

class sonata(car):
    pass
        

truck1=truck()
sedan1=sedan()
sonata1=sonata()
print("트럭-->",end="")
truck1.upspeed(200)
print("승용차-->",end="")
sedan1.upspeed(200)
print("소나타-->",end="")
sonata1.upspeed(150)



#1
class car:
    color=""
    speed=0
    def upspeed(self,value):
        self.speed+=value
    def downspeed(self,value):
        self.speed-=value

#2
class car:
    color=""
    speed=0
mycar1=car()
mycar1.color="빨강"
mycar1.speed=30

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다."%(mycar1.color,mycar1.speed))

#3
class car:
    speed=0
    def __init__(self):
        self.speed=50

a=car()
a.speed

#4
class car:
    speed=0
    def upspeed(self,value):
        self.speed+=value
        
class rvcar(car):
    seatnum=0
    def getseatnum(self):
        return self.seatnum
 






