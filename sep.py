"""class maths:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.add = num1 + num2
        self.minus = (num1-num2)
    
    def sum(self):
        print("sum of two numbers are:", self.add)
    def sub(self):
        print("subtraction of two numbers are:", self.minus)

p1 = maths(11,5)
p1.sum()   
p2 = maths(11,66)
p2.sub()"""     


##################  Sort the list based on how close the number is to 50:  #############

"""def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)"""

###############################################################################################
"""
import mathmodule

p1 = mathmodule.maths(11,5)
p1.sum()   
p2 =mathmodule.maths(11,66)
p2.sub()"""

###############################################################################################
"""class numbers:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        if num3==num2==num1:
            print("all are same value")
        elif num1>num3 and num1>num2:
            print(num1, "is greater than others number")
        elif num2>num1 and num2>num3:
            print(num2," is greatest")
        else:
            print(num3," is greatest")
        
m1 = numbers(30,200,10)"""

############################################################################################
"""import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))"""

############################################################################################

"""def onlitposnum(n):
    if n > 0:
        print("your number is correct")
    else:
        if n < 0:
            raise Exception("no negative number")

onlitposnum(int(input()))"""


"""f = open("demo.txt", "w")
f.write("lol")
f.close()
f = open("demo.txt")
print(f.read())"""



"""def main(arr):
    out = []
    x = 1
    d = 2
    x=x/d
    out.append(x)
    return out"""

"""x = int(input())
y = int(input())
z = int(input())
n = int(input())
arr = []
for i  in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if (i + j + k) !=n:
                arr.append([i,j,k])
print(arr)         
[print([[i,j,k] for i  in range(x+1) for j in range(y+1) for k in range(0,z+1) if (i + j + k) !=n])]

"""
"""n = 1
import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a[:,n])"""

##############      hakerrank python  debugging

"""1---if year % 400 == 0:
month[2] = 29
2---elif year % 100 == 0:
month[2] = 28
3---x = x * 10000 + y1
4---if x % 4 == 0 or x % 7 == 0:
5---m1 =1



def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1#1st change
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2#2nd change
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 #3rd change

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return"""

"""def arraysum(a):
    print(sum(list(map(int,a.split()))))  


a = "1 2 3 4 5 "
arraysum(a)"""