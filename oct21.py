"""
for i in range(5):
    print(i,end ='')
else:
    print("end")
"""

"""
a = []
x = input().split()
a.append(x)
print(a)
"""
"""
a ={  "x": 30,
      "y": 304,
      "z": 301
    }
for i in a:
    print(i,a[i])
"""   

"""
a ={  "x": 30,
      "y": 304,
      "z": 301
    }
temp = []  
for i,j in a.items():
    temp.append((j,i))
    temp=sorted(temp,reverse=True)
print(temp,end="")
"""

"""
a ={  "x": 30,
      "y": 304,
      "z": 301
    }
temp = []  
for i,j in a.items():
    temp.append((j,i))
    temp=sorted(temp)
print(temp,end="")
"""

"""
n = 12
j=0
for i in range(1,n,2):
    j+=1
    print(j,":",i)
"""

"""
def new_func():
    x= list((50,)*4)
    print(x)

new_func()
"""

"""
from copy import deepcopy
from  random import randint
def shuffle_list(lst):
    temp_list = deepcopy(lst)
    m = len(temp_list)
    while (m):
        m -= 1
        i = randint(0,m)
        temp_list[m],temp_list[i] = temp_list[i],temp_list[m]
        return temp_list
nums = [1,2,3,4,5,6,7,8,9]
print(nums)
print(shuffle_list(nums))
"""

"""
import random
nums = [1,2,3,4,5,6,7,8,9]

random.shuffle(nums)
print(nums)
"""

"""
def new_func():
    p = (2,3,4,5,6)
    print(p[1:-2])
    print(p[1:3])

new_func()
"""


"""for i in range(5):
    print((i+1)*'1')"""

"""def sum_arr():
    A = [8,7,6,5,4]  
    s = 0 
    for i in A:
        s += i
    print(s)

sum_arr()      """

"""
def swap_case(s):
    w =""
    for word in s:
        words = word.swapcase()
        w = w + words
        
    return w
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)   """
 ############################  or    ##########
"""def swap_case(s):
    w = s.swapcase()    
    return w  
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)  """    

"""
def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)"""

"""
string = "abracadabra"
l = list(string)
print(l)
l[5] = 'k'
string = ''.join(l)
print(string)"""
"""
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
"""  

"""
s = input()
print(any(s.isalnum() for s in s))
print(any(s.isalpha() for s in s))
print(any(s.isdigit() for s in s))
print(any(s.islower() for s in s))
print(any(s.isupper() for s in s))
"""
"""
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
"""

"""
s = "satya prakaSh"
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)"""

"""
import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
"""

"""
for i in range(1,int(input())+1):
    print(i,oct(i)[2:],hex(i)[2:].upper(),bin(i)[2:])
"""

"""
def add(n):
    return n+n
def mul(n):
    return n*n



number = [1,2,3,4]
result = map(add,number)
print(list(result))
"""

nums = [1,2,3,4]
result = map(lambda x: x+(x*2), nums)
print(list(result))
