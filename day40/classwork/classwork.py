list = []
even = []
odd = []
for i in range(10):
    numbers = int(input("enter your number:"))
    list.append(numbers)
for i in range(len(list)):
   if  list[i] % 2 == 0:

    even.append(list[i])
else:

    odd.append(i)
print(even)
print(odd)  
# len -სიგრძე
