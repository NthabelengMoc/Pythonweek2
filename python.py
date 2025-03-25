my_list =[]
my_list.append(40)
my_list.append(10)
my_list.append(30)
my_list.append(20)
# print (my_list) -used to test the code 

my_list.insert(1,15)
# print(my_list) -used to test the code 

my_list.extend([50,70,60])
print(my_list)

my_list.remove(70)
# print(my_list)

my_list.sort()
print(my_list)

index= my_list.index(30)
print(f"The index of 30 is : {index}")

print(f"Final list: {my_list}")