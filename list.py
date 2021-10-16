##############################    adding in lst    ##################
"""healthy_food = ['fruits', "vegetables", 'pizza',"salad"]

healthy_food.append("milk")   #append is a method

print(healthy_food,len(healthy_food))""" #len is a function

########## CHECKING IF ELEMENT IN LIST #########


#Obviously on our health adventures we want to know if something is healthy.
"""healthy = ["pizza", "frozen custard"]
print("chicken pot pie" in healthy)"""


######################   searching in list  #####################

"""stored_food=['maggi','eggs',"bread"]
if "jam" not in stored_food:
    print("buy the missing item")"""

####################    remove data from list   ###############

"""healthy_food = ['fruits', "vegetables", 'milk',"salad"]
stored_food = ['pizza','noodles', "burger"]

stored_food.remove("burger",)

if "pizza" not in healthy_food:
    stored_food.remove("pizza")

print(stored_food)"""

################   remove all items of stored_food if not present in healthy_food  #######
"""
healthy_food = ['fruits', "vegetables", 'pizza',"salad",'dry fruits','sweats']
stored_food = ['pizza','noodles', "burger",'fruits', "vegetables"]

# print the id of list before operation
print(id(stored_food))
#2442781199552  id before the operation


# here [:] is use to store the id of the list so id is not change after the iperation 
stored_food[:] = [item.upper() for item in stored_food if item in healthy_food]# this is example of list comprehension

#print the id after the operation, and id is unchanged 
print(id(stored_food))
#2442781199552     id after the operation

print(stored_food)

healthy_stored_food = []
for item in stored_food:
    if item in healthy_food:
        healthy_stored_food.append(item)


print(healthy_stored_food)
#['pizza', 'fruits', 'vegetables']"""


################  for print  square of number ########
"""
square=[]
for i in range(1,10):
    if i % 2 == 0: # for printing  only even number
        square.append(i**2)
print(square)    
#[4, 16, 36, 64]
#or by using list comprehension

square=[i**2 for i in range(1,10)]
print(square)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
########### length of list ###########

#print(len(['hello','hi','nmaskar']))

"""fruit = ['mango','banana','apple','orange']
index = 0
while index<len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index+1"""

            # or by for loop

"""fruit = ['mango','banana','apple','orange']
for i in range(len(fruit)):
    print(i,fruit[i])""" 

###########  count the number of repeated items in a list ###########
"""
bagpack = ['pen','pensil','namkeen','book','book','copy','copy','box','pen','pen']
print(bagpack.count("pen"))
print(bagpack.count("book"))

if bagpack.count("copy")<4:
    bagpack.append("copy")
print(bagpack.count("copy"))"""

###############################   set  ################
##################### no duplicate ####################
# to remove duplicate or repeated items
"""
bagpack = ['pen','pensil','namkeen','book','book','copy','copy','box','pen','pen']
bagpack2 = {'pen','pensil','namkeen','book','copy','copy','box','pen'}

print(bagpack2)
print("book" in bagpack2)"""

##############   count element using counter ##########
"""
from collections import Counter

bagpack = ['pen','pensil','namkeen','book','book','copy','copy','box','pen','pen','pen','pen''pen','pen',
            'chesse','potato','chips','choclate','icecream','brush','pensil','pensil','pensil','pensil',
            'chesse','potato','chips','choclate','icecream','brush','pen','pen','pensil','pensil',
            'phone','chord','cloths','fruits','razer','ink','mouse','wire','pensil','pensil',
            'phone','chord','cloths','fruits','razer','ink','mouse','wire','chesse','potato','chips',
            'choclate','icecream','brush','pen','pen','pensil','pensil','pensil','pensil','pensil',
            'phone','chord','cloths','fruits','razer','ink','mouse','wire''pensil','pensil','pensil',]

            
[print(bagpack.count(item), item)for item in set(bagpack)]      

print(Counter(bagpack))            #counter function is good way
"""

#####    replace the items but keep the id and not keep the id #####

"""bagpack = ['pen','pensil','namkeen','book','book','copy','copy','box','pen','pen','pen','pen''pen','pen',
            'chesse','potato','chips','choclate','icecream','brush','pensil','pensil','pensil','pensil',
            'chesse','potato']
print(id(bagpack))
#bagpack[:] = [1,5,58,8] # this will overide the bagpack but keep the id
#print(id(bagpack))  
bagpack = [1,2,3,4,5,6,8,9,9]  #this also do same but dont keep the id
print(id(bagpack))  
print(bagpack) """  


#####################  remove multiple items of same string ################

"""bagpack = ['pen','pensil','namkeen','book','book','copy','copy','box','pen','pen','pen','pen','pen','pen',
            'chesse','potato','chips','choclate','icecream','brush','pensil','pensil','pensil','pensil',
            'chesse','potato']
print(id(bagpack))
new_bagpack=[]
for items in bagpack:
    if items != "pen":
        new_bagpack.append(items)  #this will remove all the desired itms and copy again but not keep id
bagpack = new_bagpack  #for keeping the id use  bagpack[:] = new_bagpack 
print(id(bagpack))
print(bagpack) """       


########################### useing list-comprehension method   #############

"""bagpack = ['pen','pensil','namkeen','book','book','copy','copy','box','pen','pen','pen','pen''pen','pen',
            'chesse','potato','chips','choclate','icecream','brush','pensil','pensil','pensil','pensil',
            'chesse','potato','chips','choclate','icecream','brush','pen','pen','pensil','pensil']
print(id(bagpack))
bagpack[:] = [item for item in bagpack if item != "pen"]
print(id(bagpack))
print(bagpack)"""

###############   revere a list   #############################

"""data = [0,1,2,3,4,5,[9,8,5,4,3,2,1]]
data.reverse()
print(data)"""

#########################  swap the list #####################

"""data = ["a","v","kk","d","ld","q","w","e"]

index = 3

print(data[index],data[-index-1])

data[index], data[-index-1] = data[-index-1], data[index]

print(data[index],data[-index-1])"""


####################

"""data = ["a","v","kk","d","ld","q","w","e"]

for index in range(len(data)//2):
    print(data[index],data[-index-1])
    data[index], data[-index-1] = data[-index-1], data[index]
print(data[index],data[-index-1])"""
