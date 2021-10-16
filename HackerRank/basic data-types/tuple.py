a = []
n = int(input())
integer_list = map(int, input().split())
for x in integer_list:
    a.append(x)
y = tuple(a)    
print(hash(y))